from django import forms


class LoginForms(forms.Form):
    nome_login = forms.CharField(
        max_length=100,
        label='Login',
        required=True,
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Ex.: João Silva'}
        ),
    )
    senha = forms.CharField(
        max_length=70,
        label='Senha',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Digite a seu senha',
            }
        ),
    )


class CadastroForms(forms.Form):
    nome_cadastro = forms.CharField(
        label='Nome Completo',
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Ex.: João da Silva Sauro',
            }
        ),
    )

    email = forms.EmailField(
        label='E-mail',
        max_length=100,
        required=True,
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Ex.: joaosilva@xpto.com',
            }
        ),
    )

    senha = forms.CharField(
        label='Senha',
        max_length=70,
        required=True,
        widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'Digite sua senha'}
        ),
    )

    senha_confirma = forms.CharField(
        label='Confirmar Senha',
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Digite sua senha novamente',
            }
        ),
    )

    def clean_nome_cadastro(self):
        nome - self.cleaned_data.get('nome_cadastro')

        if nome:
            nome = nome.strip()
            if ' ' in nome:
                raise forms.ValidationError(
                    'Espaços não são permitidos nesse campo'
                )
            else:
                return nome

    def clean_senha_confirma(self):
        senha = self.cleaned_data.get('senha')
        senha_confirma = self.cleaned_data.get('senha_confirma')

        if senha and senha_confirma:
            if senha != senha_confirma:
                raise forms.ValidationError('Senhas não são iguais.')
            else:
                return senha_confirma
