from django.shortcuts import render, get_object_or_404,redirect
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from .models import BoardMember 
from django.db.models import Count

# Create your views here.

def departmentview(request):
    departments = Department.objects.all()
    staff_members = Staff.objects.all()
    total_sections_count = sum(
        department.divisions.aggregate(total_sections=models.Sum('sections__id'))['total_sections'] or 0
        for department in departments
    )

    context= {'departments': departments,
              'staff_members': staff_members, 
              'total_sections_count': total_sections_count,}
    return render(request, 'core/department_list.html', context)



def departmentdetail(request, pk):
    department = get_object_or_404(Department, pk=pk)
    sections = Section.objects.filter(division__department=department)
    staff_members = Staff.objects.filter(section__in=sections)
    divisions_with_staff_count = Division.objects.filter(department=department) \
    .annotate(total_staff_count=Count('sections__staff_members'))

    total_staff_count = staff_members.count()
     
    context = {'departments': department,
               'staff_members': staff_members,
               'div_staff_count':divisions_with_staff_count,
               'staffs':total_staff_count
               }

    return render(request, 'core/department_detail.html', context)

    
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

