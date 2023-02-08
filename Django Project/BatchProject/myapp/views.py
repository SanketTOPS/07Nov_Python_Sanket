from django.shortcuts import render,redirect
from .forms import signupForm,updateForm,notesform,feedbackForm
from .models import userSignup
from django.contrib.auth import logout
from django.core.mail import send_mail
from BatchProject import settings

# Create your views here.

def index(request):
    user=request.session.get('user')
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
    return render(request,'index.html',{'user':user})

def profile(request):
    uid=request.session.get('userid')
    user=request.session.get('user')
    cuser=userSignup.objects.get(id=uid)
    if request.method=='POST':
        updateuser=updateForm(request.POST)
        if updateuser.is_valid():
            updateuser=updateForm(request.POST,instance=cuser)
            updateuser.save()
            print("Your profile has been updated!")
        else:
            print(updateuser.errors)
    return render(request,'profile.html',{'user':user,'cuser':userSignup.objects.get(id=uid)})

def notes(request):
    user=request.session.get('user')
    if request.method=='POST':
        mynote=notesform(request.POST,request.FILES)
        if mynote.is_valid():
            mynote.save()
            print("Your notes has been uploaded!")
        else:
            print(mynote.errors)
    return render(request,'notes.html',{'user':user})

def about(request):
    return render(request,'about.html')

def contact(request):
    if request.method=='POST':
        feedback=feedbackForm(request.POST)
        if feedback.is_valid():
            feedback.save()

            # Email Sending Code
            sub="Thank you!"
            msg=f"Dear User\n\n We got your feedback!\n Thank you for your interest, we will assist you in shortly.\nIf you have any query regarding, so feel free to contact us!\n\n+91 9724799469 | sanket.tops@gmail.com"
            fromEmail=settings.EMAIL_HOST_USER
            #toEmail=["montu.marakana9919@gmail.com","ravaiyahardik@gmail.com","chaudharitejash32@gmail.com","masuraarjan0106@gmail.com","vaniyavrutika214@gmail.com","sadariyagaurav789@gmail.com"]
            toEmail=[request.POST['email']]
            send_mail(subject=sub,message=msg,from_email=fromEmail,recipient_list=toEmail)
            print("Your feedback send successfully!")
        else:
            print(feedback.errors)
    return render(request,'contact.html')

def userlogout(request):
    logout(request)
    return redirect('/')


