from django.shortcuts import render,redirect
from home.models import Employees

# Create your views here.
def index(request):
    emp = Employees.objects.all() #  by this query it will retrive all objects
    if request.method=="GET":
        st=request.GET.get('searchname')
        if st != None:
            emp=Employees.objects.filter(name__icontains=st)
    
    context = {    # variable value mapping that is passed to a template.
        'emp':emp,  #Context processors let you specify a number of variables that get set in each context automatically – without you having to specify the variables in each render() call.
    }
    return render(request,"index.html",context)


def ADD(request):
    if request.method=="POST":
        name= request.POST.get('name')
        email= request.POST.get('email')
        address= request.POST.get('address')
        phone= request.POST.get('phone')
        
        emp =Employees(
            
            name=name,#1st red name is from database name
            email=email, #2nd green name is  our input name in index file
            address= address,
            phone=phone
        )
        emp.save()
        return redirect('home')
        
        
    return render(request,"index.html")



def EDIT(request):
    emp=Employees.objects.all()
    
    context = {
        'emp':emp,
    }
    return redirect  (request,"index.html",context)

def UPDATE(request,id):
    if request.method=="POST":
        name= request.POST.get("name")
        email= request.POST.get("email")
        address= request.POST.get("address")
        phone= request.POST.get("phone")
        
        emp=Employees(
            id=id,
            name=name,
            email=email,
            address=address,
            phone=phone,
        )
        emp.save()
        return redirect('home')
    return redirect(request,"index.html")


def DELETE(request,id):
    emp=Employees.objects.filter(id=id)
    emp.delete()
    
    context = {
        'emp':emp,
    }
    
    return redirect('home')
    
    
def back(request):
    return redirect('home')
