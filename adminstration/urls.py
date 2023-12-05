from django.urls import path
from . import views
from .views import *


app_name = 'adminstration'
urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('staffs/', views.staffs, name='staffs'),
    path('boardmembers/', views.boardmembers, name='boardmembers'),
    path('create_board_member/', views.create_board_member, name='create_board_member'),
    path('create_department/', views.create_department, name='create_department'),
    path('departments/', views.departments, name='departments'),
    path('departments/<int:department_id>/', views.department, name='department'),
    path('divisions/', views.divisions, name='divisions'),
    path('department/<int:pk>/edit/', department_edit, name='dep_edit'),
    path('delete_staff/<int:user_id>/',
         views.delete_staff, name='delete_staff'),
    
]