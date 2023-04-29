from django import forms

from apps.galeria.models import Fotografia


class FotografiaForms(forms.ModelForm):
    class Meta:
        model = Fotografia
        exclude = ['publicada']
        labels = {
            'descricao': ' Descrição',
            'data_fotografia': 'Data de publicação',
            'usuario': 'Usuário',
        }
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'legenda': forms.TextInput(attrs={'class': 'form-control'}),
            'categoria': forms.Select(attrs={'class': 'form-control'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control'}),
            'foto': forms.FileInput(attrs={'class': 'form-control'}),
            'data_fotografia': forms.DateInput(
                format='%d/%b/%Y',
                attrs={'type': 'date', 'class': 'form-control'},
            ),
            'usuario': forms.Select(attrs={'class': 'form-control'}),
        }
