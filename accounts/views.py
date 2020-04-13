""" Views for pages in accounts app """

from django.shortcuts import render, redirect
from django.contrib import messages
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
    
    form = ApplicationForm()
    context = {
        'form': form
    }

    return render(request, 'application.html', context)