
from django.urls import path

from registerapp import views

urlpatterns = [
    path('register',views.register,name="register"),
    path('login',views.login,name="login"),
    path('logout',views.logout,name="logout"),
    path('menu',views.menu,name='menu'),
    path('form', views.form, name='form')

]