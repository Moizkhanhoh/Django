from django.shortcuts import render,HttpResponse
from datetime import datetime
from home.models import  Contact 
from django.contrib import messages  
# Create your views here.
def index(request):
    return render(request , 'index.html' )
def About(request):
    return render(request , 'About.html' )

def contact(request):
    if request.method == "POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        
        contact=Contact(name=name,email=email,phone=phone,date=datetime.today())
        contact.save()
        messages.success(request, 'Message has been sent!') 
        
    return render(request , 'contact.html' )

def Services(request):
    return render(request , 'Services.html' )