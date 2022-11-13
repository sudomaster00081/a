
from django.shortcuts import redirect, render

from user.views import dashboard


# Create your views here.
def home(request):
    return render(request, 'Dashboardbase.html')

def companion(request):
    #return redirect(dashboard)
    return render(request, 'companion.html')

def plantrip(request):
    return render(request, 'plantrip.html')


def chat(request):
    return render(request, 'chat.html')

def blog(request):
    return render(request, 'blog.html')

def profile(request):
    return render(request, 'profile.html')

