from django.views.generic import ListView, DetailView, UpdateView
from .models import Task, Assignment
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from notifications.models import Notification
from django.shortcuts import render, redirect, get_object_or_404
from .forms import TaskUpdateForm
from django.contrib.auth.decorators import login_required
from datetime import date
from events.models import Event
from django.utils import timezone
from news.models import News
from polls.models import Poll
from django.db.models import F


class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'tasks/dashboard_home.html'
    context_object_name = 'tasks'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Get tasks assigned to the logged-in user that are not complete
        user = self.request.user
        assigned_tasks = Task.objects.filter(assignments__assigned_to=user, assignments__completed=False)

        # Get unread notifications for the current user
        notifications = Notification.objects.filter(user=user, read=False)

        # Get upcoming events
        upcoming_events = Event.objects.filter(event_date__gt=timezone.now(), is_approved=True).order_by('event_date')

        # Get news
        news = News.objects.all().order_by('-date_posted')[:5]
        #get the polls
        latest_poll_list = Poll.objects.filter(pub_date__lte=timezone.now(), end_date__gte=timezone.now()).order_by(F('pub_date').asc())

        context['assigned_tasks'] = assigned_tasks
        context['notifications'] = notifications
        context['upcoming_events'] = upcoming_events
        context['news'] = news
        context['polls'] = latest_poll_list
        return context

   


class TaskDetailView(LoginRequiredMixin, DetailView):
    model = Task
    template_name = 'tasks/task_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = TaskUpdateForm(instance=self.object)
        
        # Calculate number of days before due date
        today = date.today()
        due_date = self.object.due_date
        days_before_due = (due_date - today).days

        # Check whether task is due today or has passed
        if due_date == today:
            context['due_message'] = "This task is due today!"
        elif due_date < today:
            context['due_message'] = "This task is past due!"
        else:
            context['due_message'] = f"This task is due in {days_before_due} days."
        
        return context


@login_required
def update_task_status(request, pk):
    task = get_object_or_404(Task, pk=pk)

    # Check if the user is assigned to the task
    try:
        assignment = Assignment.objects.get(task=task, assigned_to=request.user)
    except Assignment.DoesNotExist:
        return redirect('tasks:task_detail', pk=pk)

    if request.method == 'POST':
        form = TaskUpdateForm(request.POST, instance=task)
        if form.is_valid():
            # Update the task status
            task = form.save()

            # Mark the task as completed if status is "Complete"
            if task.status == 'C':
                assignment.completed = True
                assignment.save()

            # Redirect to the task detail page
            return redirect('tasks:task_detail', pk=pk)
    else:
        form = TaskUpdateForm(instance=task)

    context = {
        'form': form,
        'task': task,
    }
    return render(request, 'tasks/task_detail.html', context)
