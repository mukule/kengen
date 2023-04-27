from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import Department, Staff
from django.contrib.auth.decorators import login_required
from .models import BoardMember 

# Create your views here.



class departmentview(ListView):
    model = Department
    template_name = 'core/department_list.html'
    context_object_name = 'departments'


class departmentdetail(DetailView):
    model = Department
    template_name = 'core/department_detail.html'
    context_object_name ='departments'

    
    
def staff_detail(request, username):
    staff = get_object_or_404(Staff, user__username=username)
    return render(request, 'core/staff_detail.html', {'staff': staff})

class BoardMemberListView(ListView):
    model = BoardMember
    template_name = 'core/board.html'
    context_object_name = 'board_members'

class BoardMemberDetailView(DetailView):
    model = BoardMember
    template_name = 'core/board_detail.html'
    context_object_name = 'board_member'