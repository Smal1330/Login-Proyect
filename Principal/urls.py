
from django.urls import path
from .views import home,contacto
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import login,logout_then_login




urlpatterns = [
    
    path('',home, name='home'),
    path('contacto/',login_required(contacto), name='contacto'),

]

