from django import http
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.core.mail import send_mail

from django.core.files.storage import FileSystemStorage
from doctor.models import Doctor

# Create your views here.
from .forms import PatientForm, DoctorForm, PharmacyForm,LoginForm, FeedbackForm
from patient.models import Patient
from doctor.models import Doctor
from pharmacy.models import Pharmacy

def CheckToLogin(request):
    try:
        a=request.session['username']
        print(a)
        if a is None:
            return None
        else:
            pro=request.session['profession']
            return pro
    except:
        return None

def RegisterPage(request):
    pro=CheckToLogin(request)
    if(pro=='patient'):
        return redirect('cushome')
    elif (pro=='doctor'):
        return redirect('dochome')
    elif (pro=='pharmacy'):
        return redirect('pharmacyhome')
    return render(request,"Register.html")

def ContactPage(request):
    pro=CheckToLogin(request)
    if(pro=='patient'):
        return redirect('cushome')
    elif (pro=='doctor'):
        return redirect('dochome')
    elif (pro=='pharmacy'):
        return redirect('pharmacyhome')
    conform=FeedbackForm()
    if request.method=="POST":
        conform=FeedbackForm(request.POST)
        print(conform.data)
        if conform.is_valid():
            conform.save()
            return render(request,"contactus.html",{'feed':'Feedback Was Sent Successfully'})
    return render(request,"contactus.html",{'form':conform})

def AboutPage(request):
    pro=CheckToLogin(request)
    if(pro=='patient'):
        return redirect('cushome')
    elif (pro=='doctor'):
        return redirect('dochome')
    elif (pro=='pharmacy'):
        return redirect('pharmacyhome')
    return render(request,'aboutus.html')

def HomeView(request):
    pro=CheckToLogin(request)
    if(pro=='patient'):
        return redirect('cushome')
    elif (pro=='doctor'):
        return redirect('dochome')
    elif (pro=='pharmacy'):
        return redirect('pharmacyhome')
    # if(CheckToLogin(request)):
    #     return redirect(request.session['profession'])
    return render(request,'index.html')

def LoginDoctello(request):
    pro=CheckToLogin(request)
    if(pro=='patient'):
        return redirect('cushome')
    elif (pro=='doctor'):
        return redirect('dochome')
    elif (pro=='pharmacy'):
        return redirect('pharmacyhome')
    lform=LoginForm()
    if request.method=="POST":
        details=LoginForm(request.POST)
        useremail=details.data['email']
        userpass=details.data['password']
        if(useremail=="admin@gmail.com" and userpass=="admin"):
            return redirect("adminhome")
        try:
            cus=Patient.objects.get(email=useremail,password=userpass)
            AddSession1(request,cus)
            # send_mail('Login For Doctello','<h1>Thank you for login</h1>','imranirfanalikhan786@gmail.com',[useremail])
            return redirect('cushome')
        except:
            try:
                doc=Doctor.objects.get(email=useremail,password=userpass)
                print(doc.assign)
                if(doc.assign=='True'):
                    AddSession2(request,doc)
                    return redirect('dochome')
                else:
                    return render(request,'invaliduser.html')
            except:
                try:
                    med=Pharmacy.objects.get(email=useremail,password=userpass)
                    if(med.assign=='True'):
                        AddSession3(request,med)
                        return redirect('pharmacyhome')
                    else:
                        return render(request,'invaliduser.html')
                except:
                    return render(request,'login.html',{'form':details,'error':'Invalid Email or Password'})
    return render(request,'login.html',{'form':lform})

def AddSession1(request,detail):
    obj={
        'username':detail.firstname+" "+detail.lastname,
        'email':detail.email,
        'mobile':detail.mobile,
        'profession':'patient',
        'location':detail.location
    }
    request.session['username']=detail.firstname+" "+detail.lastname
    request.session['email']=detail.email
    request.session['mobile']=detail.mobile
    request.session['location']=detail.location
    request.session['profession']='patient'

def AddSession2(request,detail):
    obj={
        'username':detail.firstname+" "+detail.lastname,
        'email':detail.email,
        'mobile':detail.mobile,
        'profession':'doctor',
        'location':detail.location
    }
    request.session['username']=detail.firstname+" "+detail.lastname
    request.session['email']=detail.email
    request.session['mobile']=detail.mobile
    request.session['location']=detail.location
    request.session['profession']='doctor'

def AddSession3(request,detail):
    obj={
        'username':detail.username,
        'email':detail.email,
        'mobile':detail.mobile,
        'profession':'pharmacy',
        'location':detail.location
    }
    request.session['username']=detail.username
    request.session['email']=detail.email
    request.session['mobile']=detail.mobile
    request.session['location']=detail.location
    request.session['profession']='pharmacy'
    # print(request.session['username'],request.session['email'],request.session['mobile'],request.session['location'],request.session['profession'])

def PatientReg(request):
    pro=CheckToLogin(request)
    if(pro=='patient'):
        return redirect('cushome')
    elif (pro=='doctor'):
        return redirect('dochome')
    elif (pro=='pharmacy'):
        return redirect('pharmacyhome')
    form=PatientForm()
    if request.method=='POST':
        fform=PatientForm(data=request.POST)
        if fform.is_valid():
            fform.save()
            obj={
                'name': fform.data['firstname']+" "+fform.data['lastname'],
                'email':fform.data['email'],
                'mobile':fform.data['mobile'],
                'password':fform.data['password']
            }
            request.session['username']=fform.data['firstname']+" "+fform.data['lastname']
            request.session['email']=fform.data['email']
            request.session['mobile']=fform.data['mobile']
            request.session['location']=fform.data['location']
            request.session['profession']='patient'
            return redirect('cushome')
        return render(request,'patientRegistration.html',{'form':fform,'error':"Registration was Unsuccessful please try again"})
    return render(request,'patientRegistration.html',{'form':form})

def DoctorReg(request):
    pro=CheckToLogin(request)
    if(pro=='patient'):
        return redirect('cushome')
    elif (pro=='doctor'):
        return redirect('dochome')
    elif (pro=='pharmacy'):
        return redirect('pharmacyhome')
    dform=DoctorForm()
    if request.method=="POST":
        dform=DoctorForm(request.POST,request.FILES)
        if dform.is_valid():
            fs=FileSystemStorage()
            resume=request.FILES['resume']
            idproof=request.FILES['idproof']
            fs.save(resume.name,resume)
            fs.save(idproof.name,idproof)
            dform.save()
            return render(request,'invaliduser.html')
        return render(request,'doctorRegistration.html',{'form':dform,'error':"Registration was Unsuccessful please try again"})
    return render(request,'doctorRegistration.html',{'form':dform})

def PharmacyReg(request):
    pro=CheckToLogin(request)
    if(pro=='patient'):
        return redirect('cushome')
    elif (pro=='doctor'):
        return redirect('dochome')
    elif (pro=='pharmacy'):
        return redirect('pharmacyhome')
    pform=PharmacyForm()
    if request.method=="POST":
        pform=PharmacyForm(request.POST,request.FILES)
        print(pform.is_valid())
        if pform.is_valid():
            fs=FileSystemStorage()
            resume=request.FILES['resume']
            shopproofs=request.FILES['shopproofs']
            n1=fs.save(resume.name,resume)
            n2=fs.save(shopproofs.name,shopproofs)
            pform.save()
            # send_mail('Registing For Doctello','<h1>Thank you for registering for Doctello</h1>','yourmail',[request.POST['email']])
            return render(request,'invaliduser.html')
        return render(request,'pharmacyRegistration.html',{'form':pform,'error':"Registration was Unsuccessful please try again"})
    return render(request,'pharmacyRegistration.html',{'form':pform})

def LogoutDoctello(request):
    try:
        del request.session['username']
        del request.session['email']
        del request.session['mobile']
        del request.session['location']
        del request.session['profession']
        return redirect('home')
    except:
        return redirect('home')




# code='''
#     <h1>Hello Sree Krishna</h1>
# '''

# def emai():
#     send_mail('Successfull registration', code,
#               'imranirfanalikhan786@gmail.com', ['maremandasreekrishna@gmail.com'], fail_silently=False)