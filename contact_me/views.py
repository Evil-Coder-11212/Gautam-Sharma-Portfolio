from django.shortcuts import render, redirect, HttpResponseRedirect
from django.urls import reverse
from .form import ContactFormData


def contact(request):
    if request.method == 'POST':
        form = ContactFormData(request.POST)
        if form.is_valid():
            # Process the form data
            form.save()
            return redirect('home')
    else:
        form = ContactFormData()
    return render(request, 'contact-me.html', {'form': form})

def redirect_to_home(request):
    return HttpResponseRedirect(reverse('home') + f'#home')

def redirect_to_aboutme(request):
    return HttpResponseRedirect(reverse('home') + f'#about-me')

def redirect_to_project(request):
    return HttpResponseRedirect(reverse('home') + f'#project')
