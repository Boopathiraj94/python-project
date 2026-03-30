from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse 
from . models import RegisterStudents
# Create your views here.
def index(request):
   students = RegisterStudents.objects.all() 
   return render(request,"index.html",context={"namelists":students})


def createStudent(request):
    
    if request.method == 'POST':
       fn = request.POST.get("fname") 
       ln = request.POST.get("lname") 
       ed = request.POST.get("emailid") 
       ct = request.POST.get("city") 
       st = request.POST.get("state") 
       zc = request.POST.get("zipcode")

       RegisterStudents.objects.create(fname=fn,lname=ln,email=ed,city=ct,state=st,zipcode=zc)
       return redirect('index')
        
    else:
       return redirect('index')
    

def deleteStudent(request,sid): 
    sstudent =  RegisterStudents.objects.get(id=sid)
    sstudent.delete()
    return redirect('index')


def updateForm(request,sid):
   sstudent =  RegisterStudents.objects.get(id=sid)
    
   return render(request,'update.html',context={"studentList":sstudent})
    

from django.shortcuts import render, redirect, get_object_or_404

def updateFormData(request, sid):
    sstudent = get_object_or_404(RegisterStudents, id=sid)

    if request.method == "POST":
        sstudent.fname = request.POST.get("fname")
        sstudent.lname = request.POST.get("lname")
        sstudent.email = request.POST.get("emailid")
        sstudent.city = request.POST.get("city")
        sstudent.state = request.POST.get("state")
        sstudent.zipcode = request.POST.get("zipcode")

        sstudent.save()
 
        return redirect("index")

    return render(request, "update.html", {"studentList": sstudent})