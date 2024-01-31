from django.urls import path,include
from .views import *

urlpatterns = [
    path('sign-up/',sign_up,name='sign_up'),
    path('sign-in/',sign_in,name='sign_in'),
    path('sign-out/',sign_out,name='sign_out'),
    path('forget-password/',forget_password,name='forget_password'),
    path('reset-password/',reset_password,name='reset_password'),
]