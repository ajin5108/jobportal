from django.shortcuts import render, redirect
from datetime import datetime, date
from .models import *
from django.http import HttpResponse
# Create your views here.
def login1(request):
    return render(request,'index.html')
def employeehomepage(request):
    return render(request,'homepage.html')
def viewjobreq(request):
    ob=jobreq.objects.filter(cid__cid__id=request.session['lid'])
    return render(request,'viewjobreq.html',{'ob':ob})
def companyhomepage(request):
    return render(request,'companyhomepage.html')
def viewjobs(request):

    if request.method=='POST' and len(request.POST['search'])!=0:
        cname=request.POST['search']
        ob=addvacancy.objects.filter(cid__cname=cname)
    else:
        ob = addvacancy.objects.all()
    return render(request,'viewjobs.html',{'ob':ob})
def companyregister(request):
    return render(request,'companylogin.html')
def adminhome(request):
    return render(request,'adminhome.html')
def reg(request):
    return render(request,'reg.html')
def index2(request):
    return render(request,'index2.html')
def addvacancy1(request):
    return render(request,'addvacancy.html')
def emphomepage(request):
    return render(request,'emphomepage.html')
def uploadcv(request,id):
    request.session['cid']=id
    return render(request,'uploadcv.html')
def sendfeed3(request):
    return render(request,'sendfeed.html')
def feed(request):
    ob = sendfeed.objects.all()
    return render(request,'feed.html',{'ob':ob})
def ar(request):
    ob=companylogin.objects.filter(cid__type="pending")
    return render(request,'ar.html',{'ob':ob})
def reject(request,id):
    ob=login.objects.get(id=id)
    ob.delete()
    return redirect('/ar')
def accept(request,id):
    ob=login.objects.get(id=id)
    ob.type="company"
    ob.save()
    return redirect('/ar')
def viewemp(request):
    ob = companylogin.objects.all()
    return render(request,'viewemp.html',{'ob':ob})
def log(request):
    ename = request.POST['ename']
    pas = request.POST['pw']
    print(ename,pas,"=============================")
    try:
        ob = login.objects.get(username=ename, password=pas)
        if ob.type=="employee":
            request.session['lid'] = ob.id
            return redirect('/viewjobs')
        elif ob.type=="company":
            request.session['lid'] = ob.id
            return redirect('/index2')
        elif ob.type=="admin":
            request.session['lid'] = ob.id
            return redirect('/adminhome')
        else:
            return HttpResponse("<script>alert('account not accepted');window.location='/';</script>")



    except Exception as e:
        print('=============',e)
        return HttpResponse("<script>alert('INVALID USERNAME OR PASSWORD');window.location='/';</script>")
def remployee(request):
    fname = request.POST['fname']
    lname = request.POST['lname']
    DOB = request.POST['dob']
    address = request.POST['adrs']
    pin = request.POST['pcode']
    phone = request.POST['num']
    uname = request.POST['uname']
    email = request.POST['email']
    gender = request.POST['gender']
    password = request.POST['pw']
    ob = login()
    ob.username = uname
    ob.password = password
    ob.type="employee"
    ob.save()
    ob1 =Employee()
    ob1.fname = fname
    ob1.lname = lname
    ob1.dob = DOB
    ob1.address = address
    ob1.email=email
    ob1.gender=gender
    ob1.pin = pin
    ob1.number = phone
    ob1.uid = login.objects.get(id=ob.id)
    ob1.save()
    return redirect('/')
def companyreg(request):
    cname = request.POST['cname']
    cregnum = request.POST['cregnum']
    cadd= request.POST['cadd']
    contact = request.POST['contact']
    website = request.POST['website']
    uname = request.POST['uname']
    password = request.POST['pw']
    ob = login()
    ob.username = uname
    ob.password = password
    ob.type="pending"
    ob.save()
    ob1 =companylogin()
    ob1.cname = cname
    ob1.cregnum = cregnum
    ob1.cadd = cadd
    ob1.contact= contact
    ob1.website= website
    ob1.cid = login.objects.get(id=ob.id)
    ob1.save()
    return redirect('/')

def addvacancy2(request):
    jt = request.POST['jt']
    vac = request.POST['vac']
    date= request.POST['date']
    skills = request.POST['skills']
    dis = request.POST['dis']

    ob1 =addvacancy()
    ob1.jt = jt
    ob1.vac = vac
    ob1.datefrom = datetime.now().strftime("%Y-%m-%d")
    ob1.dateto = date
    ob1.skills= skills
    ob1.dis= dis
    ob1.cid = companylogin.objects.get(cid__id=request.session['lid'])
    ob1.save()
    return redirect('/index2')
def sendfeed2(request):
    feedback = request.POST['feedback']


    ob1 =sendfeed()
    ob1.jt = feedback

    ob1.company = companylogin.objects.get(cid__id=request.session['lid'])
    ob1.save()
    return redirect('/index2')
def jreq(request):
    cv=request.FILES['cv']
    expsal=request.POST['exp_salary']
    ob=jobreq()
    ob.cv=cv
    ob.expsalary=expsal
    ob.eid=Employee.objects.get(uid__id=request.session['lid'])
    ob.cid=companylogin.objects.get(id=request.session['cid'])
    ob.save()
    return redirect('/emphomepage')

