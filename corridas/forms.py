from django import forms
from .models import Corridas

class CorridasForm(forms.ModelForm):
    class Meta:
        model = Corridas
        fields = ["distancia", "tempo", "data_da_corrida", "sentimento", "observacoes"]