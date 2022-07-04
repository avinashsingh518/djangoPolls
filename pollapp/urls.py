from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin', admin.site.urls),
    path('home/',views.home,name='home'),
    path('',views.profile,name='profile'),
    path('signup', views.signup, name='signup'),
    path('login', views.login, name='login'),
    path('index/', views.index, name = 'index'),
    path('vote/<str:pk>', views.vote, name = 'vote'),
    path('result/<str:pk>', views.result, name = 'result')

]