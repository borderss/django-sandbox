from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('castVote', views.castVote, name='castVote'),
]