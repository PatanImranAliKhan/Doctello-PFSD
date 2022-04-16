from django import http
from django.shortcuts import render, redirect
from django.http import HttpResponse
from authentication.forms import FeedbackForm
from .forms import HealthTipsForm, SlotForm
from .models import Consult, Doctor, HealthTips, Slot
from django.core.mail import send_mail
from datetime import date
from time import strptime
import time
# Create your views here.

def CheckProfession(request):
    try:
        a=request.session['username']
        if a is None:
            return None
        else:
            pro=request.session['profession']
            return pro
    except:
        return None

def TipsPage(request):
    pro=CheckProfession(request)
    if pro=='patient':
        return redirect('cushome')
    elif pro=='pharmacy':
        return redirect('pharmacyhome')
    tform=HealthTipsForm()
    tf=HealthTipsForm()
    if request.method=="POST":
        tform=HealthTipsForm(request.POST)
        print(tform.data['causes'])
        print(tform.is_valid())
        if tform.is_valid():
            tform.save()
            return render(request,'healthtips.html',{'form':tf,'success':'Data has been saved'})
    return render(request,'healthtips.html',{'form':tform})

def DocContactPage(request):
    pro=CheckProfession(request)
    if pro=='patient':
        return redirect('cushome')
    elif pro=='pharmacy':
        return redirect('pharmacyhome')
    conform=FeedbackForm()
    if request.method=="POST":
        conform=FeedbackForm(request.POST)
        print(conform.data)
        if conform.is_valid():
            conform.save()
            return render(request,"doccontact.html",{'feed':'Feedback Was Sent Successfully'})
    return render(request,"doccontact.html",{'form':conform})

def AboutPage(request):
    pro=CheckProfession(request)
    if pro=='patient':
        return redirect('cushome')
    elif pro=='pharmacy':
        return redirect('pharmacyhome')
    return render(request,'docabout.html')


def DoctorHomePage(request):
    pro=CheckProfession(request)
    if pro=='patient':
        return redirect('cushome')
    elif pro=='pharmacy':
        return redirect('pharmacyhome')
    try:
        c=Consult.objects.filter(doctoremail=request.session['email'],date=date.today())
        return render(request,'doctorHome.html',{'consults':c})
    except:
        return render(request,'doctorHome.html')


def SelectSlot(request):
    pro=CheckProfession(request)
    if pro=='patient':
        return redirect('cushome')
    elif pro=='pharmacy':
        return redirect('pharmacyhome')
    sform=SlotForm()
    if request.method=="POST":
        request.session['username']
        sform=SlotForm(request.POST)
        try:
            s=Slot.objects.get(email=request.session['email'],location=request.session['location'],date=sform.data['date'],slot=sform.data['slot'])
            return render(request,'selectslot.html',{'form':sform,'error':'slot was booked already'})
        except:
            s=Slot(email=request.session['email'],location=request.session['location'],date=sform.data['date'],slot=sform.data['slot'])
            s.save()
            return render(request,'selectslot.html',{'form':sform,'success':'slot was booked successfully'})
    return render(request,'selectslot.html',{'form':sform})


def SlotsListPage(request):
    dt=date.today()
    try:
        print(request.session['email'])
        slots=Slot.objects.filter(email=request.session['email'],date__gte=dt)
        return render(request,'listofslots.html',{'slots':slots})
    except:
        return render(request,'listofslots.html')

def month_string_to_number(s):
    s=s.strip()[:3].lower()
    m = {
        'jan':'01',
        'feb': '02',
        'mar': '03',
        'apr': '04',
        'may': '05',
        'jun': '06',
        'jul': '07',
        'aug': '08',
        'sep': '09',
        'oct': '10',
        'nov': '11',
        'dec': '12'
    }
    return m[s]

def UpdateSlotPage(request,dt):

    if "update" in request.POST:
        sform=SlotForm(request.POST)
        print(sform.data['date'],"   ",sform.data['slot'],"  ",dt)
        data=Slot.objects.filter(email=request.session['email'],date=dt)
        data.update(date=sform.data['date'],slot=sform.data['slot'])
        return redirect('slotslist')
    slot=request.POST.get('slot')
    print(dt,"  ",slot)
    sform=SlotForm(request.POST,initial={'slot':slot,'date':dt})
    return render(request,'updateslot.html',{'form':sform,'date':dt})

def ConsultsPage(request):
    pro=CheckProfession(request)
    if pro=='patient':
        return redirect('cushome')
    elif pro=='pharmacy':
        return redirect('pharmacyhome')
    try:
        consults=Consult.objects.filter(doctoremail=request.session['email'])
        return render(request,'allconsults.html',{'consults':consults})
    except:
        return render(request,'allconsults.html')


def ViewDetails(request,name,email,date):
    consults=Consult.objects.filter(useremail=email)
    problem=Consult.objects.get(useremail=email,doctoremail=request.session['email'],date=date).problem
    if request.method=="POST":
        c=Consult.objects.filter(username=name,useremail=email,doctoremail=request.session['email'],date=date)
        c.update(status=request.POST['status'])
        return render(request,'viewcusdetails.html',{'consults':consults,'name':name,'email':email,'date':date,'success':'feedback was sent'})
    return render(request,'viewcusdetails.html',{'consults':consults,'name':name,'email':email,'date':date,'problem':problem})

def LogoutDoctello(request):
    del request.session['username']
    del request.session['email']
    del request.session['mobile']
    del request.session['location']
    del request.session['profession']
    return redirect('home')


def TodaysConsultations(request):
    c=Consult.objects.filter(date=date.today())
    print(c)


def DoctorProfilePage(request):
    pro=CheckProfession(request)
    if pro=='patient':
        return redirect('cushome')
    elif pro=='pharmacy':
        return redirect('pharmacyhome')
    doct=Doctor.objects.get(email=request.session['email'])
    print(doct)
    password=doct.password
    if request.method=="POST" and "update" in request.POST:
        m=request.POST['mobile']
        mob=""
        if(len(m)==10):
            mob=request.POST['mobile']
        else:
            mob=request.session['mobile']
        if(request.POST['oldpass']!="" and request.POST['oldpass']!=doct.password):
            return render(request,'docprofile.html',{'doctor':doct,'errorp':'incorrect password'})
        if(request.POST['newpass']!="" and request.POST['newpass']!=request.POST['confirmpass']):
            return render(request,'docprofile.html',{'doctor':doct,'errorcon':'password wasnot matched'})
        if(request.POST['newpass']==""):
            password=doct.password
        else:
            password=request.POST['newpass']
        request.session['username']=request.POST['firstname']+" "+request.POST['lastname']
        request.session['mobile']=mob
        doct=Doctor.objects.filter(email=request.session['email'])
        doct.update(firstname=request.POST['firstname'],lastname=request.POST['lastname'],mobile=mob,password=password)
        doct=Doctor.objects.get(email=request.session['email'])
        return render(request,'docprofile.html',{'doctor':doct,'success':'successfully updated the data'})
    return render(request,'docprofile.html',{'doctor':doct})

def DoctorUpdateProfilePic(request):
    try:
        u = Doctor.objects.get(email=request.session['email'])
        u.profilepic = request.FILES['profilepic']
        u.save()
        return redirect('doctorprofile')
    except:
        return redirect('login')

# import time

# t = time.localtime()
# current_time = time.strftime("%H:%M:%S", t)
# print(current_time)

# import datetime

# x = datetime.datetime.now()

# print(x.strftime("%H"))

# import datetime
# >>> now = datetime.datetime.now()
# >>> today8am = now.replace(hour=8, minute=0, second=0, microsecond=0)
# >>> now < today8am
# True
# >>> now == today8am
# False
# >>> now > today8am
# False