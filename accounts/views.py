""" Views for pages in accounts app """
from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render, redirect

from .forms import UserRegisterForm, ApplicationForm

# Create your views here.
def register_view(request):
    """
    View for users to register a new account.
    Checks if form is valid, and responds accordingly,
    then redirects users to the login page on successfully
    creating a new account.
    """
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created {username}. You can now log in.')

            return redirect('login')
    else:
        form = UserRegisterForm()

    context = {
        "form": form,
    }
    return render(request, 'register.html', context)

def profile_view(request):
    return render(request, 'profile.html')

def pitch_view(request):
    return render(request, 'pitch.html')

def application_view(request):
    """
    View to handle applications for new businesses. Redirects logged in
    users to home page. If not logged in, renders form to apply.
    """
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == "POST":
        form = ApplicationForm(request.POST)

        if form.is_valid():
            form.save()

            contact_name = form.cleaned_data.get('contact_name')
            email = form.cleaned_data.get('email')
            business_name = form.cleaned_data.get('business_name')
            message = form.cleaned_data.get('message')
            kvk_num = form.cleaned_data.get('kvk_num')
            
            # Sends email to manager when new business applies to advertise
            subject = f'New application to FamilyHub from {business_name}'
            full_message = f'Business Name: {business_name}\nKVK number: {kvk_num}\nContact Name: {contact_name}\nEmail: {email}\n\nMessage: {message}'
            from_email = email
            to_list = [settings.EMAIL_HOST_USER]

            send_mail(subject, full_message, from_email, to_list, fail_silently=True)

            # sends message to user on submitting form
            messages.success(
                request, f'Thank you {contact_name}, your application has been submitted for review. You will receive a response within 2 working days to {email}.'
            )
            return redirect('home')
    
    else:
        form = ApplicationForm()

    context = {
        'form': form
    }

    return render(request, 'application.html', context)