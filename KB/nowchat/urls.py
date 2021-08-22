from django.urls import path
from . import views

urlpatterns = [
    path('', views.nowChat, name='clchat'),
    path('<str:who>/<int:clid>/', views.addChat, name='addchat'),
]
