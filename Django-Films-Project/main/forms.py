from .models import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth import get_user_model
from django import forms


class AddFilmForm(forms.ModelForm):
    class Meta:
        model = Film
        fields = ['film_name', 'film_description', 'film', 'file', 'picture']
        widgets = {
            'film_name': forms.TextInput(attrs={'class': 'form-control', 'aria-label': 'Sizing example input', 'aria-describedby': 'inputGroup-sizing-sm'}),
            'film': forms.TextInput(attrs={'class': 'form-control', 'aria-label': 'Sizing example input', 'aria-describedby': 'inputGroup-sizing-sm'}),
            'film_description': forms.Textarea(attrs={'class': 'form-control', 'rows': '3'}),
            'file': forms.FileInput(attrs={'class': "form-control form-control-sm", 'data-bs-theme': 'dark'}),
            'picture': forms.FileInput(attrs={'class': "form-control form-control-sm", 'data-bs-theme': 'dark'})
        }


class AddCommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['comment']
        widgets = {
            'comment': forms.Textarea(attrs={'class': "comments-area"})
        }


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label='Имя',
        widget=forms.TextInput(attrs={'class': 'form-control', 'aria-label': 'Sizing example input', 'aria-describedby': 'inputGroup-sizing-sm'})
    )

    password = forms.CharField(
        label = 'Пароль',
        widget=forms.PasswordInput(render_value=False, attrs={'class': 'form-control', 'aria-label': 'Sizing example input', 'aria-describedby': 'inputGroup-sizing-sm'})
    )


class ChangePassForm(PasswordChangeForm):
    error_messages = {
        'password_incorrect': 'Ваш старый пароль введен неверно. Пожалуйста, введите снова.'
    }

    old_password = forms.CharField(
        label='Старый пароль',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'aria-label': 'Sizing example input', 'aria-describedby': 'inputGroup-sizing-sm'})
    )

    new_password1 = forms.CharField(
        label='Новый пароль',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'aria-label': 'Sizing example input', 'aria-describedby': 'inputGroup-sizing-sm'})
    )

    new_password2 = forms.CharField(
        label='Повтор',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'aria-label': 'Sizing example input', 'aria-describedby': 'inputGroup-sizing-sm'})
    )


class RegisterUserForm(UserCreationForm):
    error_messages = {
        'password_mismatch': 'Пароли не совпадают'
    }

    username = forms.CharField(
        label='Имя пользователя',
        widget=forms.TextInput(attrs={'class': 'form-control', 'aria-label': 'Sizing example input', 'aria-describedby': 'inputGroup-sizing-sm'})
    )

    password1 = forms.CharField(
        label='Пароль',
        widget=forms.PasswordInput(render_value=False, attrs={'class': 'form-control', 'aria-label': 'Sizing example input', 'aria-describedby': 'inputGroup-sizing-sm'})
    )

    password2 = forms.CharField(
        label='Повтор паторя',
        widget=forms.PasswordInput(render_value=False, attrs={'class': 'form-control', 'aria-label': 'Sizing example input', 'aria-describedby': 'inputGroup-sizing-sm'})
    )

    class Meta:
        model = Users
        fields = ['username', 'password1', 'password2']
        widgets = {
            'password1': forms.PasswordInput(),
            'password2': forms.PasswordInput()
        }

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = 'Ник'
        self.fields['username'].attrs = {'class': 'form-control', 'aria-label': 'Sizing example input', 'aria-describedby': 'inputGroup-sizing-sm'}

