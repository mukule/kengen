from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import SetPasswordForm
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.forms import UserChangeForm
from .models import *
from core.models import *
from ckeditor.widgets import CKEditorWidget


class StaffForm(UserCreationForm):
    username = forms.CharField(
        max_length=30,
        widget=forms.TextInput(attrs={'placeholder': 'Username', 'class': 'form-control'}),
        label='',
    )
    email = forms.EmailField(
            max_length=254,
            widget=forms.EmailInput(attrs={'placeholder': 'Email', 'class': 'form-control'}),
            label='',
        )
    first_name = forms.CharField(
            max_length=30,
            widget=forms.TextInput(attrs={'placeholder': 'Enter First Name', 'class': 'form-control'}),
            label='',
        
        )
    last_name = forms.CharField(
        max_length=30,
        widget=forms.TextInput(attrs={'placeholder': 'Enter Last Name', 'class': 'form-control'}),
        label='',
        
    )
    gender = forms.ModelChoiceField(
        queryset=Gender.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control', 'id': 'gender'}),
        label='Gender',
        required=False,
    )
    marital_status = forms.ModelChoiceField(
        queryset=MaritalStatus.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control', 'id': 'marital_status'}),
        label='Marital Status',
        required=False,
    )
    title = forms.ModelChoiceField(
        queryset=Honorific.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control', 'id': 'title'}),
        label='Title',
        required=False,
    )
    access_level = forms.ChoiceField(
        choices=CustomUser.ACCESS_LEVEL_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control', 'id': 'access_level'}),
        label='Access Level',
    )
    image = forms.ImageField(
        widget=forms.FileInput(attrs={'class': 'form-control', 'id': 'image'}),
        label='Image',
        required=False,
    )
    about = forms.CharField(
        widget=CKEditorWidget(attrs={'class': 'form-control', 'rows': 3}),
        label='About',
        required=False,
    )

    biography = forms.CharField(
        widget=CKEditorWidget(attrs={'class': 'form-control', 'rows': 3}),
        label='Biography',
        required=False,
    )

    career = forms.CharField(
        widget=CKEditorWidget(attrs={'class': 'form-control', 'rows': 3}),
        label='Career',
        required=False,
    )

    skills = forms.CharField(
        widget=CKEditorWidget(attrs={'class': 'form-control', 'rows': 3}),
        label='Skills',
        required=False,
    )

    other_roles = forms.CharField(
        widget=CKEditorWidget(attrs={'class': 'form-control', 'rows': 3}),
        label='Other Roles',
        required=False,
    )

    interests = forms.CharField(
        widget=CKEditorWidget(attrs={'class': 'form-control', 'rows': 3}),
        label='Interests',
        required=False,
    )
    department = forms.ModelChoiceField(
        queryset=Department.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control', 'id': 'department'}),
        label='Department',
        required=False,
    )
    division = forms.ModelChoiceField(
        queryset=Division.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control', 'id': 'division'}),
        label='Division',
        required=False,
    )
    section = forms.ModelChoiceField(
        queryset=Section.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control', 'id': 'section'}),
        label='Section',
        required=False,
    )
    location = forms.ModelChoiceField(
        queryset=Location.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control', 'id': 'location'}),
        label='Location',
        required=False,
    )

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'first_name', 'last_name',
                  'gender', 'marital_status', 'title', 'access_level', 'image',
                  'about', 'biography', 'career', 'skills', 'other_roles', 'interests', 'section']

    
class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    username = forms.CharField(
        label='username',
        widget=forms.TextInput(attrs={'placeholder':'Staff Number', 'class':'form-control'})
    )

    password = forms.CharField(
        label='',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
    



class SetPasswordForm(SetPasswordForm):
    class Meta:
        model = get_user_model()
        fields = ['new_password1', 'new_password2']

class PasswordResetForm(PasswordResetForm):
    def __init__(self, *args, **kwargs):
        super(PasswordResetForm, self).__init__(*args, **kwargs)

class CustomUserChangeForm(UserChangeForm):
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput,
        required=False,
    )

    class Meta:
        model = get_user_model()
        fields = '__all__'

