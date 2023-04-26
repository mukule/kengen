from django import forms
from django.contrib import admin
from .models import Staff, Section
from django.forms import ModelForm

class SectionModelChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return f"{obj.name} ({obj.division.department.name} - {obj.division.name})"

class StaffAdminForm(forms.ModelForm):
    section = SectionModelChoiceField(queryset=Section.objects.all())

    class Meta:
        model = Staff
        fields = '__all__'


class StaffUpdateForm(forms.ModelForm):
    job_type = forms.CharField(max_length=100, required=False)
    education = forms.CharField(max_length=100, required=False)
    professional_associations = forms.CharField(widget=forms.Textarea, required=False)
    position = forms.CharField(max_length=100, required=False)
    bio = forms.CharField(widget=forms.Textarea, required=False)
    personal_interest = forms.CharField(widget=forms.Textarea, required=False)
    work_history = forms.CharField(widget=forms.Textarea, required=False)
    career_statement = forms.CharField(widget=forms.Textarea, required=False)
    skills = forms.CharField(widget=forms.Textarea, required=False)
    awards = forms.CharField(widget=forms.Textarea, required=False)

    class Meta:
        model = Staff
        fields = ['job_type', 'education', 'professional_associations', 'position', 'bio',
                  'personal_interest', 'work_history', 'career_statement', 'skills', 'awards']