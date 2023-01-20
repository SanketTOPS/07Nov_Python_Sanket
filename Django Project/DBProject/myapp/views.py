from django.shortcuts import render,redirect
from .forms import userinfoForm
from .models import userInfo

# Create your views here.

def index(request):
    if request.method=='POST':
        newuser=userinfoForm(request.POST)
        if newuser.is_valid():
            newuser.save()
            print("Data inserted!")
        else:
            print(newuser.errors)
    return render(request,'index.html')

def showdata(request):
    stdata=userInfo.objects.all()
    return render(request,'showdata.html',{'stdata':stdata})

def updatedata(request,id):
    stid=userInfo.objects.get(id=id)
    if request.method=='POST':
        updateuser=userinfoForm(request.POST)
        if updateuser.is_valid():
            updateuser=userinfoForm(request.POST,instance=stid)
            updateuser.save()
            print("Your data has been updated!")
            return redirect('showdata')
        else:
            print(updateuser.errors)
    return render(request,'updatedata.html',{'stid':userInfo.objects.get(id=id)})

def deletedata(request,id):
    stid=userInfo.objects.get(id=id)
    userInfo.delete(stid)
    return redirect('showdata')

