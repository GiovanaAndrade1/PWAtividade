from django.urls import path
from . import views


urlpatterns = [
    path('', views.Atividade2, name = 'Atividade2'),
]