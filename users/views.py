from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.contrib.auth import get_user_model
from .forms import SetPasswordForm
from .forms import PasswordResetForm
from .decorators import user_not_authenticated
from django.db.models.query_utils import Q
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from .token import account_activation_token
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.utils.html import strip_tags
from django.core.mail import EmailMultiAlternatives
from core.forms import StaffUpdateForm
from django.shortcuts import render, redirect, get_object_or_404
from users.models import CustomUser
from users.forms import *

from django.http import HttpResponse
import secrets
from django.template.loader import render_to_string
from django.utils.http import urlencode
from django.core.mail import send_mail
import random
import string
from users.forms import *


# # Create your views here.
# def register(request):
#     # if request.user.is_authenticated:
#     #     return redirect('/')

#     if request.method == "POST":
#         form = UserRegisterForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             messages.success(request, f"New account created: {user.username}")
#             return redirect('login')

#         else:
#             for error in list(form.errors.values()):
#                 messages.error(request, error)

#     else:
#         form = UserRegisterForm()

#     return render(
#         request=request,
#         template_name = "users/register.html",
#         context={"form": form}
#         )


def generate_random_password(length=10):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def add_staff(request):
    if request.method == 'POST':
        form = StaffForm(request.POST, request.FILES,)
        if form.is_valid():
            user = form.save()

            # Generate a random 8-digit password
            password = generate_random_password()

            # Update the user's password
            user.set_password(password)
            user.save()

            # Send email with login details
            send_details(user, password)

            # Add success message
            messages.success(request, f"{user.username}'s staff account has been created successfully. Login details have been sent to {user.email}.")

            return redirect('adminstration:staffs') 
        else:
            # Add error messages to the form
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"Error in {field}: {error}")
    else:
        form = StaffForm()
        
    context = {'form': form}
    return render(request, 'adminstration/create_staff.html', context)

def send_details(user, password):
    subject = 'Staff Account Created Successfully'
    message = render_to_string('adminstration/details.html', {'user': user, 'password': password})
    from_email = 'nelson.masibo@kenyaweb.com'
    to_email = user.email

    # Send the email
    send_mail(subject, message, from_email, [to_email])



def custom_login(request):
    if request.method == "POST":
        form = UserLoginForm(request=request, data=request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data["username"],
                password=form.cleaned_data["password"],
            )
            if user is not None:
                login(request, user)
                # messages.success(request, f"You are logged in as <b>{user.username}</b>")
                return redirect('tasks:dashboard_home')

        else:
            for error in list(form.errors.values()):
                messages.error(request, error) 

    form = UserLoginForm()

    return render(
        request=request,
        template_name="users/login.html",
        context={"form": form}
        )




@login_required
def profile(request, username):
    user = get_object_or_404(CustomUser, username=username)
    if request.method == 'POST':
        form = StaffUpdateForm(request.POST, request.FILES, instance=user.staff)
        if form.is_valid():
            staff_form = form.save(commit=False)
            image = form.cleaned_data['image']
            if image:
                staff_form.user.image = image
                staff_form.user.save()
            staff_form.save()

            messages.success(request, f'{staff_form.user.first_name}, Your profile has been updated!')
            return redirect('core:staff_detail', staff_form.user.username)

        for error in list(form.errors.values()):
            messages.error(request, error)

    form = StaffUpdateForm(instance=user.staff)
        
    return render(request, 'users/profile.html', context={'form': form, 'user': user})



@login_required
def password_change(request):
    user = request.user
    username = request.user.username
    if request.method == 'POST':
        form = SetPasswordForm(user, request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your password has been changed")
            return redirect('profile', username= username)
        else:
            for error in list(form.errors.values()):
                messages.error(request, error)

    form = SetPasswordForm(user)
    return render(request, 'users/password_reset_confirm.html', {'form': form})

@user_not_authenticated
def password_reset_request(request):
    if request.method == 'POST':
        form = PasswordResetForm(request.POST)
        
        if form.is_valid():
            user_email = form.cleaned_data['email']
            associated_user = get_user_model().objects.filter(Q(email=user_email)).first()
            if associated_user:
               subject = "Password Reset request"
               html_message = render_to_string("users/template_reset_password.html", {
                   'user': associated_user,
                   'domain': get_current_site(request).domain,
                   'uid': urlsafe_base64_encode(force_bytes(associated_user.pk)),
                   'token': account_activation_token.make_token(associated_user),
                   "protocol": 'https' if request.is_secure() else 'http'
                   })
               plain_message = strip_tags(html_message)
               email = EmailMultiAlternatives(subject, plain_message, to=[associated_user.email])
               email.attach_alternative(html_message, "text/html")
               email.send()
               if email.send():
                messages.success(request,"""Password reset has been emailed to you please check your mail""")
            else:
                messages.error(request, "Problem sending reset password email, <b>An authentic error occurred/b>")

            return redirect('index')

        for key, error in list(form.errors.items()):
            if key == 'captcha' and error[0] == 'This field is required.':
                messages.error(request, "You must pass the reCAPTCHA test")
                continue

    form = PasswordResetForm()
    return render(
        request=request, 
        template_name="users/password_reset.html", 
        context={"form": form}
        )
def passwordResetConfirm(request, uidb64, token):
    User = get_user_model()
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except:
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        if request.method == 'POST':
            form = SetPasswordForm(user, request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "Your password has been set. You may go ahead and <b>log in </b> now.")
                return redirect('login')
            else:
                for error in list(form.errors.values()):
                    messages.error(request, error)

        form = SetPasswordForm(user)
        return render(request, 'users/password_reset_confirm.html', {'form': form})
    else:
        messages.error(request, "Link is expired")

    messages.error(request, 'Something went wrong, redirecting back to Homepage')
    return redirect("index")


@login_required
def index(request):
    user = request.user
    context = {
        'user': user
    }
    return render(request, 'users/index.html', context)

@login_required
def custom_logout(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("login")