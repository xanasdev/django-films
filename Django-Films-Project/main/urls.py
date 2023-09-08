from django.urls import path
from django.contrib.auth.views import LogoutView

from . import views

urlpatterns = [
    path('', views.Index.as_view(), name='main'),
    path('register/', views.RegisterUser.as_view(), name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('login/', views.LoginUser.as_view(), name='login'),
    path('account/', views.PersonalArea.as_view(), name='lk'),
    path('account/change_password', views.ChangePassword.as_view(), name='changepassword'),
    path('panel/', views.AdminPanel.as_view(), name='adminpanel'),
    path('panel/add_film/', views.AddFilm.as_view(), name='add-film'),
    path('watch/<str:film>', views.WatchFilm.as_view(), name='watch'),
    path('add-comment/<str:film>', views.add_comment, name='add-comment')
]
