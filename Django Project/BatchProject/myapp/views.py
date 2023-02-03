from django.shortcuts import render,redirect
from .forms import signupForm
from .models import userSignup
from django.contrib.auth import logout

# Create your views here.

def index(request):
    if request.method=='POST': #root
        if request.POST.get('signup')=='signup':
            newuser=signupForm(request.POST)
            if newuser.is_valid():
                newuser.save()
                print("User created successfully!")
                return redirect('/')
            else:
                print(newuser.errors)
        elif request.POST.get('login')=='login':
            unm=request.POST['username']
            pas=request.POST['password']

            userid=userSignup.objects.get(username=unm)
            print("UserID:",userid.id)
            user=userSignup.objects.filter(username=unm,password=pas)
            if user:
                print("Login Successfull!")
                request.session['userid']=userid.id
                request.session['user']=unm
                return redirect('notes')
            else:
                print("Error!Login faild")
    return render(request,'index.html')

def profile(request):
    uid=request.session.get('userid')
    user=request.session.get('user')
    cuser=userSignup.objects.get(id=uid)
    return render(request,'profile.html',{'user':user,'cuser':userSignup.objects.get(id=uid)})

def notes(request):
    user=request.session.get('user')
    return render(request,'notes.html',{'user':user})

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def userlogout(request):
    logout(request)
    return redirect('/')