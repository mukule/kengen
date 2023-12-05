from django.shortcuts import render, redirect, get_object_or_404
from core.models import *
from .forms import *
from django.contrib import messages
from.forms import *

# Create your views here.

def dashboard(request):
    return render(request, 'adminstration/index.html')

def boardmembers(request):
    # Retrieve all board members from the database
    board_members = BoardMember.objects.all()

    # Pass the retrieved board members to the template
    context = {'board_members': board_members}
    return render(request, 'adminstration/boardmembers.html', context)

def create_board_member(request):
    if request.method == 'POST':
        form = BoardMemberCreateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Board member added successfully.')  # Success message
            return redirect('adminstration:boardmembers')
        else:
            messages.error(request, 'Error adding board member. Please check the form.')  # Error message
    else:
        form = BoardMemberCreateForm()

    context = {'form': form}
    return render(request, 'adminstration/create_board_member.html', context)

def create_department(request):
    if request.method == 'POST':
        form = DepartmentCreateForm(request.POST, request.FILES,)
        if form.is_valid():
            form.save()
            return redirect('adminstration:departments')  # Redirect to a list view of departments
    else:
        form = DepartmentCreateForm()

    context = {'form': form}
    return render(request, 'adminstration/create_department.html', context)


def department_edit(request, pk):
    department = get_object_or_404(Department, pk=pk)
    
    if request.method == 'POST':
        form = DepartmentCreateForm(request.POST, request.FILES, instance=department)
        if form.is_valid():
            form.save()
            return redirect('adminstration:department', department_id=department.pk)
    else:
        form = DepartmentCreateForm(instance=department)

    return render(request, 'adminstration/dep_edit.html', {'form': form, 'department': department})

def departments(request):
    departments = Department.objects.all()
    context = {'departments': departments}
    return render(request, 'adminstration/departments.html', context)

def department(request, department_id):
    department = get_object_or_404(Department, pk=department_id)
    divisions = department.divisions.all()  # Retrieve related divisions for the department
    context = {'department': department, 'divisions': divisions}
    return render(request, 'adminstration/department.html', context)

def divisions(request):
    if request.method == 'POST':
        form = DivisionCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('division_list')  # Redirect to a list view of divisions
    else:
        form = DivisionCreateForm()

    context = {'form': form}
    return render(request, 'division/create_division.html', context)

def create_section(request):
    if request.method == 'POST':
        form = SectionCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('section_list')  # Redirect to a list view of sections
    else:
        form = SectionCreateForm()

    context = {'form': form}
    return render(request, 'section/create_section.html', context)






def staffs(request):
    users = CustomUser.objects.all()
    context = {'users': users}
    return render(request, 'adminstration/staffs.html', context)

def delete_staff(request, user_id):
    user = get_object_or_404(CustomUser, pk=user_id)

    user.delete()
    return redirect('adminstration:staffs')