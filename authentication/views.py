from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, logout, login
# Create your views here.


def index(request):
    return render(request, "index.html")


def signup(request):
    if (request.method == "POST"):
        username = request.POST["username"]
        email = request.POST.get("email", False)
        password = request.POST["password"]

        if User.objects.filter(email=email):
            messages.error(request, "Email is already taken!")
            return redirect("signup")
        if User.objects.filter(username=username):
            messages.error(request, "Username is already taken!")
            return redirect("signup")

        user = User.objects.create_user(username, email, password)

        user.save()
        messages.success(request, "Successfully created a accout")
        return render(request, "login.html")
    return render(request, "signup.html")


def login_(request):
    if (request.method == "POST"):
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)

        if user is not None:
            messages.success(request, "Logged in successfully")
            login(request, user)
            return render(request, "index.html")
        else:

            messages.error(request,"Accout does not exist!")
            return redirect("signup")
    return render(request, "login.html")


def logout_(request):
    logout(request)
    messages.success(request,"Successfully logged out!")
    return redirect("home")

