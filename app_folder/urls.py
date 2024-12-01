from django.urls import path
from . import views

app_name = 'app_folder'
urlpatterns = [
  path('top', views.top, name='top')
]