from django.shortcuts import render, redirect
from django.contrib.auth import logout as auth_logout
from django.views.generic import TemplateView

def login(request):
    context = {}
    template = 'login.html'
    return render(request, template, context)

def home(request):
    context = {}
    template = 'home.html'
    return render(request, template, context)

def logout(request):
    auth_logout(request)
    return redirect('/')

class HomeView(TemplateView):
    template_name = "home.html"

