from django.urls import path
from . import views
from .views import departmentview, departmentdetail, staffdetail, BoardMemberListView, BoardMemberDetailView


app_name = 'core'
urlpatterns = [
    path('department', departmentview.as_view(), name='departmentview'),
    path('<int:pk>', departmentdetail.as_view(), name='departmentdetail'),
    path('<int:pk>/', staffdetail.as_view(), name='staffdetail'),
    path('board-members/', BoardMemberListView.as_view(), name='board_member'),
     path('board-members/<int:pk>/', BoardMemberDetailView.as_view(), name='board_detail'),
]
   
  
