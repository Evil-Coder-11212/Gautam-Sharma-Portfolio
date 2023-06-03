from django.urls import path, include
from .views import get_data
from .views import BlogsDetail
from . import views
urlpatterns = [
    path("blogs", get_data.as_view(), name="blogs"),
    path("blogs/<int:pk>", BlogsDetail.as_view(), name="blog-details"),
    path("blogs/blogs", views.redirect_to_blog, name="redirected"),
    path('home/', views.redirect_to_home, name='home'),
    path('project/', views.redirect_to_project, name='project'),
    path('about-me/', views.redirect_to_aboutme, name='about-me'),
    path('blogs/about-me', views.redirect_to_aboutme, name='about-me'),
    path('blogs/project', views.redirect_to_project, name='project'),
    ]