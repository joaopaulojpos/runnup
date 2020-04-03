from django.shortcuts import render, redirect
from .models import Corridas
from .forms import CorridasForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
#from django.contrib import messages


@login_required()
def dashboard(request):
    if request.method == 'POST':
        form = CorridasForm(request.POST)
        if form.is_valid():
            formu = form.save(commit=False)
            formu.corredor = request.user
            formu.save()
            return redirect('dashboard')
    else:
        form = CorridasForm()

    corridas = Corridas.objects.filter(corredor=request.user)
    return render(request, 'dashboard.html', {'corridas':corridas, 'form':form})



def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form':form})