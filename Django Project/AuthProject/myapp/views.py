from django.shortcuts import render,redirect
from .forms import signupForm
from .models import usersignup
from django.contrib.auth import logout

# Create your views here.
def index(request):
    if request.method=='POST':
        unm=request.POST['username']
        pas=request.POST['password']

        user=usersignup.objects.filter(username=unm,password=pas)
        if user: #true
            print("Login successfully!")
            request.session["user"]=unm #create a session
            return redirect('home')
        else:
            print("Error!Login faild")
    return render(request,'index.html')

def signup(request):
    if request.method=='POST':
        newuser=signupForm(request.POST)
        if newuser.is_valid():
            newuser.save()
            print("User created successfully!")
            return redirect('home')
        else:
            print(newuser.errors)
    return render(request,'signup.html')

def home(request):
    user=request.session.get('user')
    return render(request,'home.html',{'user':user})

def userlogout(request):
    logout(request)
    return redirect('/')
    