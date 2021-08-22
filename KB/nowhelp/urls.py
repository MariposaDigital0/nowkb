from django.urls import path
from . import views

urlpatterns = [
    path('', views.nowHelp, name='nowhelp'),
]
