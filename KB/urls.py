from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='KB.home'),
    path('searchresults/', views.searchresults, name='searchresults'),
    path('info/<str:name>/', views.info, name="info"),
    path('nowhelp/', include('KB.nowhelp.urls')),
    path('clchat/', include('KB.nowchat.urls')),
]
