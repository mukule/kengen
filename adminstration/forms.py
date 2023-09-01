from django import forms
from django.forms import ClearableFileInput
from core.models import *
from.models import *

class BoardMemberCreateForm(forms.ModelForm):
    role = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Enter role'}))
    details = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Enter details'}))

    class Meta:
        model = BoardMember
        fields = ['name', 'image', 'role', 'details']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter name'}),
            'image': ClearableFileInput(attrs={'class': 'form-control-file'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['image'].required = False  # Set image field as not required

class DepartmentCreateForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['name', 'hod', 'mandate', 'charter', 'vision', 'strategy', 'description', 'performance_score']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter department name'}),
            'hod': forms.Select(attrs={'class': 'form-control'}),
            'mandate': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter department mandate'}),
            'charter': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'vision': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'strategy': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter department description'}),
            'performance_score': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter performance score'}),
        }

class DivisionCreateForm(forms.ModelForm):
    class Meta:
        model = Division
        fields = ['name', 'hod', 'department', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter division name'}),
            'hod': forms.Select(attrs={'class': 'form-control'}),
            'department': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter division description'}),
        }

class SectionCreateForm(forms.ModelForm):
    class Meta:
        model = Section
        fields = ['name', 'hod', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter section name'}),
            'hod': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter section description'}),
        }

class StaffCreateForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = ['user', 'date_started', 'job_type', 'education', 'position']
        widgets = {
            'user': forms.Select(attrs={'class': 'form-control'}),
            'date_started': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'YYYY-MM-DD'}),
            'job_type': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter job type'}),
            'education': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter education'}),
            'position': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter position'}),
        }