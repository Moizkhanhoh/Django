from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate,login

# passward for user owais is mardan1122@

# Create your views here.
def index(request):
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request,'index.html')
    
    
def loginuser(request):#now check user give coreect email and password for login??
    if request.method=="POST":
        username=request.POST.get('username')
        password= request.POST.get('password')
        # print(username,password)
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect("/")
        else:
            return render(request,'login.html')
        
    return render(request,'login.html')

def logoutuser(request):
    logout(request)
    return redirect("/login")
      
    return render(request,'logout.html')
    