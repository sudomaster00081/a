
from django.shortcuts import redirect, render

from user.views import dashboard


# Create your views here.
def home(request):
    return render(request, 'dashboard\Dashboardbase.html')

def companion(request):
    #return redirect(dashboard)
    return render(request, 'dashboard\companion.html')

def plantrip(request):
    return render(request, 'dashboard\plantrip.html')


def chat(request):
    return render(request, 'dashboard\chat.html')

def blog(request):
    return render(request, "dashboard\pblog.html")

def profile(request):
    return render(request, 'dashboard\profile.html')

