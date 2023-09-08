from .models import *


class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs

        return context


class FilmsMixin:

    def get_user_context(self, **kwargs):
        context = kwargs

        films = Film.objects.all()

        context['film'] = films

        return context


class GetFilm:

    def get_user_context(self, id, **kwargs):
        context = kwargs

        film = Film.objects.filter(film=id)[0]
        comments = Comments.objects.filter(film=film.pk)
        print(film)
        print(id)
        print(comments)
        context['comments'] = comments
        context['film'] = film
        context['title'] = film.film_name

        return context
