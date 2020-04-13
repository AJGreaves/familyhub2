from django.contrib.auth import views as auth_views
from django.urls import path
from .views import register_view, profile_view, pitch_view, application_view

urlpatterns = [
    path('register/', register_view, name="register"),
    path('login/', auth_views.LoginView.as_view(
        template_name='login.html',
        redirect_authenticated_user=True), name="login"),
    path('logout/', auth_views.LogoutView.as_view(
        template_name='logout.html'), name="logout"),
    path('profile/', profile_view, name="profile"),
    path('for-businesses/', pitch_view, name="pitch"),
    path('apply/', application_view, name="apply")
]
