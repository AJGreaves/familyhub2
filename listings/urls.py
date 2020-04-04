from django.urls import path
from .views import (
    clubs_view,
    educational_view,
    events_view,
    parties_view
)

urlpatterns = [
    path('clubs/', clubs_view, name="clubs"),
    path('educational/', educational_view, name="educational"),
    path('events/', events_view, name="events"),
    path('parties/', parties_view, name="parties"),
]