
from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup_user, name='signup_user'),
    path('login/', views.login_user, name='login_user'),
    path('logout/', views.logout_user, name='logout_user'),
    path('category/<str:category_name>/', views.category_view, name='category'),
    path('download_book/<int:id>/', views.download_book, name='download_book'),
    path('search/', views.search, name='search'),
]
