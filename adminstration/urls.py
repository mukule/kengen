from django.urls import path
from . import views
from .views import *


app_name = 'adminstration'
urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('boardmembers/', views.boardmembers, name='boardmembers'),
]