from django.urls import path
from . import views

# URL configuration/ URLconf
urlpatterns = [
    path('hello/', views.say_hello)
]