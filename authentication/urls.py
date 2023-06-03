from django.urls import path
from . import views
urlpatterns = [
    path("login", views.login_, name="login"),
    path("signup", views.signup, name="signup"),
    path("logout", views.logout_, name="logout"),
    path("", views.index, name="home"),
]
