from django.shortcuts import render
from .forms import userinfoForm

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