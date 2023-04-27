from django.urls import path
from . import views
from .views import departmentview, departmentdetail, staff_detail, BoardMemberListView, BoardMemberDetailView

app_name = 'core'

urlpatterns = [
    path('department', departmentview.as_view(), name='departmentview'),
    path('<int:pk>', departmentdetail.as_view(), name='departmentdetail'),
    path('board-members/', BoardMemberListView.as_view(), name='board_member'),
    path('board-members/<int:pk>/', BoardMemberDetailView.as_view(), name='board_detail'),
    path('staff/<str:username>/', staff_detail, name='staff_detail'),
]
