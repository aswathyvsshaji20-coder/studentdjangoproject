from django.shortcuts import render,redirect
from django.http import HttpResponse
from datetime import *
from Projectsampleapp.forms import *
from Projectsampleapp.models import *
# Create your views here.
def welcome(request):
    return HttpResponse("Welcome To Django Sample Project 2")

def one(request):
    return render(request,'index.html')

def two(request):
    return render(request,'two.html')

def three(request):
    return render(request,'three.html')

def four(request):
    return render(request,'four.html')

def five(request):
    return render(request,'fifth.html')

def sixth(request):
    data="welcome to dtl hello"
    x="Hello"
    today=datetime.now()
    return render (request,"sixth.html",{'d1':data})
    # return render(request,"sixth.html")

def nine(request):
    return render(request,"nine.html")

#crud 
#crete   -read/retreave   -update  -delete

def employeedata(request):
    if request.method=="POST":
        frm=EmployeeForm(request.POST)
        if frm.is_valid():
            frm.save()
            return HttpResponse("Succesfull")
        else:
            return HttpResponse("Failed")
    else:
        data=EmployeeForm()
        return render(request,'employeedata.html',{'x':data})
# view    
def empview(request):
    data=Employee.objects.all()
    return render(request,'Empview.html',{'x':data})

#delete 
def empdel(request,did):
    data=Employee.objects.get(id=did)
    data.delete()
    return redirect(empview)

def empedit(request,uid):
    data=Employee.objects.get(id=uid)
    return render(request,'empedit.html',{'x':data})

def empedit2(request,uid):
    if request.method=="POST":
        x=Employee.objects.get(id=uid)
        frm=EmployeeForm(request.POST,instance=x)
        if frm.is_valid():
            frm.save()
            return redirect(empview)
        return HttpResponse("Failed")

def profiledata(request):
    if request.method=="POST":
        frm=ProfileForm(request.POST,request.FILES)
        if frm.is_valid():
            frm.save()
            return HttpResponse("Succesfull")
        return HttpResponse("Failed")
    else:
        x=ProfileForm()
        return render(request,'profiledata.html',{'data':x})

def studreg(request):
    if request.method=="POST":
        nm=request.POST["Name"]
        ag=request.POST["Age"]
        em=request.POST["Email_id"]
        ph=request.POST["Phone"]
        gn=request.POST["Gender"]
        print(nm,ag,em,ph,gn)
        x=Student.objects.create(Name=nm,Age=ag,Email_id=em,Phone=ph,Gender=gn)
        x.save()
        return HttpResponse("Succesfull")
    else:
        return render(request,"studreg.html")
    
def studview(request):
    data=Student.objects.all()
    return render(request,"studview.html",{'x':data})

def studdelete(request,did):
    x=Student.objects.get(id=did)
    x.delete()
    return redirect(studview)

def studedit(request,did):
    x=Student.objects.get(id=did)
    return render(request,'studedit.html',{'data':x})

def studedit1(request,did):
    if request.method=="POST":
        nm=request.POST["Name"]
        ag=request.POST["Age"]
        em=request.POST["Email_id"]
        ph=request.POST["Phone"]
        gn=request.POST["Gender"]
    x=Student.objects.get(id=did)
    x.Name=nm
    x.Age=ag
    x.Email_id=em
    x.Phone=ph
    x.Gender=gn
    x.save()
    return redirect(studview)

def addmark(request):
    if request.method=='POST':
        sid=request.POST["sid"]
        m=request.POST["Mark"]
        g=request.POST["Grade"]
        x=AddMark.objects.create(Mark=m,Grade=g,Sid_id=sid)
        x.save()
        return HttpResponse("Success")
    else:
        x=Student.objects.all()
        return render(request,'addmark.html',{'data':x})
    
def viewmark(request):
    x=AddMark.objects.all()
    return render(request,'viewmark.html',{'data':x})

def editmark(request,did):
    x=AddMark.objects.get(id=did)
    return render(request,"editmark.html",{'data':x})

def editmark1(request,did):
    if request.method=='POST':
        mk=request.POST["Mark"]
        gd=request.POST["Grade"]
    x=AddMark.objects.get(id=did)
    x.Mark=mk
    x.Grade=gd
    x.save()
    return redirect(viewmark)

def deletemark(request,did):
    x=AddMark.objects.get(id=did)
    x.delete()
    return redirect(viewmark)

def deleteall(request,dsid):
    x=Student.objects.get(id=dsid)
    x.delete()
    return redirect(viewmark)

def setcookie(request):
    res=HttpResponse("Cookie is Set")
    res.set_cookie("Username","Ammu")
    return res
def getcookie(requets):
    uname=requets.COOKIES.get("Username")
    return HttpResponse({uname})

def setsession(request):
    request.session["username"]="ammu@gmail.com"
    return HttpResponse("Session is set")
def getsession(request):
    uname=request.session.get("username")
    return HttpResponse({uname})

def deletesession(request):
    del request.session["username"]
    return HttpResponse("Session Deleted")
"""objects.all()
objects.get"""


# def employeedata(request):
#     if request.method=
#     if request.method=="POST":
#         frm=EmployeeForm(request.POST)
#         if frm.is_valid():
#             frm.save()
#             return HttpResponse("Succesfull")
#         else:
#             return HttpResponse("Failed")

#     data=EmployeeForm()
#     return render(request,'employeedata.html',{'x':data})