from django.shortcuts import render , redirect
from django.http import HttpResponse ,JsonResponse
from django.contrib import messages
from django.contrib.auth.models import User, auth
# Create your views here.


def home(request):
    return render(request, 'homepage\Homepage.html')


def login(request):
    if request.method == 'POST':
        uname = request.POST['uname']
        paswd = request.POST['passwd']
        user = auth.authenticate(username=uname,password=paswd)
        if user is not None :
            auth.login(request, user)
            messages.info(request, 'Login Successfull')
            #return render(request, 'dashboard\Dashboard.html',{ 'result' : uname})
            return redirect('dashboard')#, { 'result' : uname})
        else :
            messages.info(request, 'Invalid Credentials')
            return render(request , 'homepage\Homepage.html')   
    else :
         return redirect('dashboard')


def signup(request):
    if request.method == 'POST' :
        uname=request.POST['suname']
        email=request.POST['email']
        pass1=request.POST['spasswd']
        #fname = request.PST['fname']
        #pass2=request.POST['pass2']
        if User.objects.filter(username=uname).exists():
            messages.info(request, 'Username Taken')
            return render(request, 'homepage\Homepage.html')
        elif User.objects.filter(email=email).exists():
            messages.info(request,'Email Taken')
            return redirect('signup')
        else :
            user = User.objects.create_user( username=uname, password=pass1, email=email)
            user.save();
            messages.info(request, 'Welcome On Board' )
            auth.login(request, user)
            return redirect('dashboard')
  
    else:
        return render(request, 'homepage\Homepage.html')
    return render(request, 'homepage\Homepage.html')


def dashboard(request):
    if request.method == 'POST':
        print("helloworld")
    
    else:
        return render(request, 'dashboard\Dashboard.html')


def logout(request):
    auth.logout(request)
    return redirect('/')

def ajlogin(request):
    if request.method == 'POST':
        uname = request.POST['uname']
        paswd = request.POST['passwd']
        user = auth.authenticate(username=uname,password=paswd)
        if user is not None :
            auth.login(request, user)
            messages.info(request, 'Login Successfull')
            #return render(request, 'dashboard\Dashboard.html',{ 'result' : uname})
            return JsonResponse(
                {'success' : True},
                safe = False
            )
        else :
            #messages.info(request, 'Invalid Credentials')
            return JsonResponse(
                {'success' : False},
                safe = False
            )  
    else :
         return render(request, 'dashboard\Dashboard.html')

