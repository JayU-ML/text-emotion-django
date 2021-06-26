from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'text'
urlpatterns = [
    path('', views.helloworldfunction, name="text"),
    path('get/', views.get, name="get"),
]
