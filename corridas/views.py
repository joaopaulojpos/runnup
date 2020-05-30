from django.shortcuts import render, redirect, get_object_or_404
from .models import Corridas
from .forms import CorridasForm,CreateUserForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.paginator import Paginator
import datetime


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

    mes = datetime.datetime.now()
    corridas = Corridas.objects.filter(corredor=request.user, data_da_corrida__month = mes.month).order_by('-data_da_corrida')
    return render(request, 'dashboard.html', {'corridas':corridas, 'form':form})


@login_required()
def run_update(request, id):
	corridas = get_object_or_404(Corridas, pk=id)
	form = CorridasForm(request.POST or None, instance=corridas)
	if form.is_valid():
		formu = form.save(commit=False)
		formu.corredor = request.user
		formu.save()
		return redirect('dashboard')
	return render(request,'run_update.html', {'corridas':corridas,'form':form})


@login_required()
def run_list(request):
	mes = datetime.datetime.now()
	corridas_list = Corridas.objects.filter(corredor=request.user, data_da_corrida__month = mes.month).order_by('-data_da_corrida')
	paginator = Paginator(corridas_list, 2)

	page = request.GET.get('page')
	corridas = paginator.get_page(page)
	return render(request, 'run_list.html', {'corridas':corridas})


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