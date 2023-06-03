from django.urls import path
from . import views

urlpatterns = [
    path("contact-me", views.contact, name="contact-me"),
    path('home', views.redirect_to_home, name='home'),
    path('project', views.redirect_to_project, name='project'),
    path('about-me', views.redirect_to_aboutme, name='about-me'),
]
