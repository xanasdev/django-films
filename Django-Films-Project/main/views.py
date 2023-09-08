from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView, PasswordChangeView

from .models import *
from .forms import *
from .utils import *


class ChangePassword(DataMixin, PasswordChangeView):
    form_class = ChangePassForm
    success_url = reverse_lazy('lk')
    template_name = 'main/changepassword.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Смена пароля')
        return dict(list(context.items()) + list(c_def.items()))


class LoginUser(DataMixin, LoginView):
    form_class = LoginForm
    template_name = 'main/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Авторизация")
        return dict(list(context.items()) + list(c_def.items()))


class AddFilm(DataMixin, CreateView):
    form_class = AddFilmForm
    template_name = 'main/add-film.html'
    success_url = reverse_lazy('adminpanel')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Панель')
        return dict(list(context.items()) + list(c_def.items()))


class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'main/register.html'
    success_url = reverse_lazy('main')

    def form_valid(self, form):
        valid = super(RegisterUser, self).form_valid(form)
        username, password = form.cleaned_data.get('username'), form.cleaned_data.get('password1')
        new_user = authenticate(username=username, password=password)
        login(self.request, new_user)
        return valid

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Регистрация')
        return dict(list(context.items()) + list(c_def.items()))


class AdminPanel(DataMixin, ListView):
    model = Users
    template_name = 'main/admin-panel.html'
    context_object_name = 'data'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Панель')
        return dict(list(context.items()) + list(c_def.items()))


class PersonalArea(DataMixin, ListView):
    model = Users
    template_name = 'main/personalarea.html'
    context_object_name = 'data'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Личный кабинет')
        return dict(list(context.items()) + list(c_def.items()))


class Index(FilmsMixin, ListView):
    model = Users
    template_name = 'main/main.html'
    context_object_name = 'data'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='TEST TV')

        return dict(list(context.items()) + list(c_def.items()))


class WatchFilm(GetFilm, ListView):
    model = Users
    template_name = 'main/watch.html'
    context_object_name = 'data'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(self.request.GET.get('film'))

        return dict(list(context.items()) + list(c_def.items()))


def add_comment(request, film):
    if request.method == "POST":
        text = request.POST.get('comment-text')
        print(film)
        new = Comments(film=Film.objects.get(film=request.GET.get('film')), comment=text)
        new.save()
        return redirect(f'/watch/url?film={request.GET.get("film")}')

    return render(request, 'main/main.html')
