"""
    Views for listings pages
"""

from django.shortcuts import render

# Create your views here.
def clubs_view(request):
    """ renders clubs page """
    return render(request, 'clubs.html')

def educational_view(request):
    """ renders educational page """
    return render(request, 'educational.html')

def events_view(request):
    """ renders events page """
    return render(request, 'events.html')

def parties_view(request):
    """ renders parties page """
    return render(request, 'parties.html')
