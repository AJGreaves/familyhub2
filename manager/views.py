from django.shortcuts import render, get_object_or_404
from accounts.models import Application

# Create your views here.
def manager_view(request):
    """
    View to handle manager page. Loads applications and displays them with a form
    to update their status. Processes status change from the manager to update
    database.
    """
    waiting_applications = Application.objects.filter(status="Awaiting response")
    denied_applications = Application.objects.filter(status="Denied")
    approved_applications = Application.objects.filter(status="Approved")
    context = {
        "waiting_applications": waiting_applications,
        "denied_applications": denied_applications,
        "approved_applications": approved_applications,
    }

    if request.method == "POST":
        form = request.POST
        Application.objects.filter(pk=form['pk']).update(status=form['status'])

    return render(request, 'manager.html', context)
    


