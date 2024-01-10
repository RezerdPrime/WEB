from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class LoginForm(forms.Form):
    username = forms.CharField(
        max_length = 100,
        widget = forms.TextInput(
            attrs = {
                'class':'form-control',
                'placeholder':'Your login',
                'aria-describedby':'basic-addon1'
            })
    )
    password = forms.CharField(
        max_length = 100,
        widget = forms.PasswordInput(
            attrs = {
                'class': 'form-control',
                'placeholder': 'Your password',
                'aria-describedby': 'basic-addon2'
            })
    )
    email = forms.EmailField(
        max_length = 100,
        widget = forms.EmailInput(
            attrs = {
                'class': 'form-control',
                'placeholder': 'Your email',
                'aria-describedby': 'basic-addon3'
            })
    )


class RegisterForm(LoginForm):
    username = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Your login',
                'aria-describedby': 'name_set'
            })
    )
    password = forms.CharField(
        max_length=100,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Your password',
                'aria-describedby': 'pass_set'
            })
    )
    password_rep = forms.CharField(
        max_length=100,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Repeat password',
                'aria-describedby': 'pass_repeat'
            })
    )
    email = forms.EmailField(
        max_length=100,
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Your email',
                'aria-describedby': 'email'
            })
    )
    planet = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Your planet',
                'aria-describedby': 'planet'
            })
    )
    gender = forms.ChoiceField(
        choices=[(1, 'parquet'), (2, 'laminate'), (3, 'helicopter boss')],
        widget=forms.Select(
            attrs={}
        )
    )
    opros = forms.MultipleChoiceField(
        choices=[(1, 'Gamma function'), (2, 'Series of inverse squares'), (3, 'Gaussian integral')],
        widget=forms.CheckboxSelectMultiple(
            attrs={}
        ),
        required=False
    )

    def clean_username(self):
        name = self.cleaned_data['username']

        name_list = User.objects.values('username')  # список свойств в формате:
        # [{'username': 'MyUsername1'}, {'username': 'MyUsername2'}, ...]
        for val in name_list:
            if name == val['username']:
                raise ValidationError('Такой username уже существует')

        return name


    def clean_password_rep(self):
        password = self.cleaned_data['password']
        password_rep = self.cleaned_data['password_rep']

        if password_rep != password:
            raise ValidationError('Пароли должны совпадать')

        return password_rep