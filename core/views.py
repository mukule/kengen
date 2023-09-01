from django.shortcuts import render, get_object_or_404,redirect
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from .models import BoardMember 

# Create your views here.

def departmentview(request):
    departments = Department.objects.all()
    staff_members = Staff.objects.all()
    
    return render(request, 'core/department_list.html', {'departments': departments, 'staff_members': staff_members})

def departmentdetail(request, pk):
    department = get_object_or_404(Department, pk=pk)
    sections = Section.objects.filter(division__department=department)
    staff_members = Staff.objects.filter(section__in=sections)

    return render(request, 'core/department_detail.html', {'departments': department, 'staff_members': staff_members})
    
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

