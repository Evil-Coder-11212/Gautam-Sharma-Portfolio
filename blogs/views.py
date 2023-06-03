from django.shortcuts import redirect, render, HttpResponseRedirect
from django.views.generic import ListView, DeleteView
from .models import Blogs
from django.urls import reverse

# Create your views here.

class get_data(ListView):
    model = Blogs
    template_name  = "blogs.html"

class BlogsDetail(DeleteView):
    model = Blogs
    template_name="blogs_details.html"

def redirect_to_blog(request):
    return redirect( "blogs")

def redirect_to_home(request):
    return HttpResponseRedirect(reverse('home') + f'#home')

def redirect_to_aboutme(request):
    return HttpResponseRedirect(reverse('home') + f'#about-me')

def redirect_to_project(request):
    return HttpResponseRedirect(reverse('home') + f'#project')
def redirect_to_contactme(request):
    return render(request, "contact-me.html")