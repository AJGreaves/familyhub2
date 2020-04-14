from django.shortcuts import render, get_object_or_404
from accounts.models import Application

# Create your views here.
def manager_view(request):
    waiting_applications = Application.objects.filter(status="Awaiting response")
    denied_applications = Application.objects.filter(status="Denied")
    approved_applications = Application.objects.filter(status="Approved")
    context = {
        "waiting_applications": waiting_applications,
        "denied_applications": denied_applications,
        "approved_applications": approved_applications,
    }
    return render(request, 'manager.html', context)

