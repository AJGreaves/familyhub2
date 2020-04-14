from django.shortcuts import render

# Create your views here.
def manager_view(request):
    return render(request, 'manager.html')