from django.shortcuts import render, redirect
from .models import Corridas
from .forms import CorridasForm,CreateUserForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import messages


@login_required()
def dashboard(request):
    if request.method == 'POST':
        form = CorridasForm(request.POST)
        if form.is_valid():
            formu = form.save(commit=False)
            formu.corredor = request.user
            formu.save()
            messages.success(request, 'Corrida Adicionada com sucesso')
            return redirect('dashboard')
    else:
        form = CorridasForm()

    corridas = Corridas.objects.filter(corredor=request.user)
    return render(request, 'dashboard.html', {'corridas':corridas, 'form':form})


def register(request):
	if request.user.is_authenticated:
		return redirect('dashboard')
	else:
		form = CreateUserForm()
		if request.method == 'POST':
			form = CreateUserForm(request.POST)
			if form.is_valid():
				form.save()
				user = form.cleaned_data.get('username')
				messages.success(request, 'Account was created for ' + user)

				return redirect('login')
			

		context = {'form':form}
		return render(request, 'registration/signup.html', context)