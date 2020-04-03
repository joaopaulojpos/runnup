from django import forms
from .models import Corridas
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CorridasForm(forms.ModelForm):
    class Meta:
        model = Corridas
        fields = ["distancia", "tempo", "data_da_corrida", "sentimento", "observacoes"]


class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']