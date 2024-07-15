from django import forms
from .models import Cadastro

class CadastroForm(forms.ModelForm):
    sobrenome = forms.CharField(max_length=100, required=True, label='Sobrenome')

    class Meta:
        model = Cadastro
        fields = ['nome', 'data_de_nascimento', 'usuario', 'senha', 'sobrenome']
        widgets = {
            'senha': forms.PasswordInput(),
        }

    def save(self, commit=True):
        instance = super(CadastroForm, self).save(commit=False)
        # Combinar nome e sobrenome
        instance.nome = f"{self.cleaned_data['nome']} {self.cleaned_data['sobrenome']}"
        if commit:
            instance.save()
        return instance 