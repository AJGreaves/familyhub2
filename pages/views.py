"""
    Views for pages that don't belong in specific apps
"""

from django.shortcuts import render

# Create your views here.
def home_view(request):
    """ renders home page """
    context = { 'page' : 'home' }
    return render(request, 'index.html', context)
