from django import forms
from .models import Etudiant

class EtudiantForm(forms.ModelForm):
    class Meta:
        model = Etudiant
        fields = ['nom','date_naissance','sexe','cin','cne','adresse','note_1ere','note_2eme']  # بلا mention
        widgets = {
            'date_naissance': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'nom': forms.TextInput(attrs={'class': 'form-control'}),
            'sexe': forms.Select(attrs={'class': 'form-select'}),
            'cin': forms.TextInput(attrs={'class': 'form-control'}),
            'cne': forms.TextInput(attrs={'class': 'form-control'}),
            'adresse': forms.TextInput(attrs={'class': 'form-control'}),
            'note_1ere': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'note_2eme': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
        }

