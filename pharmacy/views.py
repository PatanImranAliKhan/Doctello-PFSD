from django.shortcuts import render, redirect
from django.http import HttpResponse
from authentication.forms import FeedbackForm
from .forms import MedicineForm
from .models import Medicine,MedicineOrder, Pharmacy
from django.core.mail import send_mail
from sys import maxsize
from itertools import permutations
# Create your views here.

def travellingSalesmanProblem(graph,s,v):
    vertex=[]
    for i in range(v):
        if i!=s:
            vertex.append(i)
    min_path=maxsize
    next_permutation=permutations(vertex)
    for i in next_permutation:
        current_pathweight=0
        k=s
        for j in i:
            current_pathweight+=graph[k][j]
            k=j
        current_pathweight+=graph[k][s]
    min_path=min(min_path,current_pathweight)
    return min_path

def ShortestPath(request):
    l=['Anantapur','Chittoor','East Godavari','Guntur','Kadapa','Krishna','Kurnool','Nellore',
    'Prakasam','Srikakulam','Vishakapatnam','Viziayanagaram','West Godavari']
    graph=[[0,1,0,0,1,0,1,0,0,0,0,0,0],[1,0,0,0,1,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,1],[0,0,0,0,0,1,0,0,1,0,0,0,0],
            [1,1,0,0,0,0,1,1,0,0,0,0,0],[0,0,0,1,0,0,0,0,0,0,0,0,1],[1,0,0,0,1,0,0,0,1,0,0,0,0],[0,1,0,0,1,0,0,0,1,0,0,0,0],
            [0,0,0,1,1,0,1,1,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,1,0],[0,0,1,0,0,0,0,0,0,0,0,1,0],[0,0,0,0,0,0,0,0,0,0,1,0,1],
            [0,0,1,0,0,1,0,0,0,0,0,0,0]]

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

def PharmacyHomePage(request):
    pro=CheckProfession(request)
    if pro=='patient':
        return redirect('cushome')
    elif pro=='doctor':
        return redirect('dochome')
    return render(request,'med_home.html')

def AddMedicinePage(request):
    pro=CheckProfession(request)
    if pro=='patient':
        return redirect('cushome')
    elif pro=='doctor':
        return redirect('dochome')
    addform=MedicineForm()
    if request.method=="POST":
        addform=MedicineForm(request.POST)
        email=request.session['email']
        loc=request.session['location']
        med=Medicine(medicinename=addform.data['medicinename'],email=email,location=loc,startprice=addform.data['startprice'],endprice=addform.data['endprice'],image=addform.data['image'])
        med.save()
        addform=MedicineForm()
        return render(request,'addMedicines.html',{'form':addform,'success':'Medicine has been saved'})
    return render(request,'addMedicines.html',{'form':addform})

def AllMedicinesPage(request):
    medicines=Medicine.objects.filter(email=request.session['email'])
    if request.method=="POST":
        medic=request.POST.get('remove')
        med=Medicine.objects.get(medicinename=medic,email=request.session['email'])
        med.delete()
        medicines=Medicine.objects.filter(email=request.session['email'])
        return render(request,'allmedicines.html',{'medicines':medicines,'success':'Medicine was deleted successfully'})
    return render(request,'allmedicines.html',{'medicines':medicines})

def ContactPage(request):
    pro=CheckProfession(request)
    if pro=='patient':
        return redirect('cushome')
    elif pro=='doctor':
        return redirect('dochome')
    conform=FeedbackForm()
    if request.method=="POST":
        conform=FeedbackForm(request.POST)
        print(conform.data)
        if conform.is_valid():
            conform.save()
            return render(request,"medcontact.html",{'feed':'Feedback Was Sent Successfully'})
    return render(request,"medcontact.html",{'form':conform})

def AboutPage(request):
    pro=CheckProfession(request)
    if pro=='patient':
        return redirect('cushome')
    elif pro=='doctor':
        return redirect('dochome')
    return render(request,'medabout.html')

def OrdersPage(request):
    pro=CheckProfession(request)
    if pro=='patient':
        return redirect('cushome')
    elif pro=='doctor':
        return redirect('dochome')
    try:
        orders=MedicineOrder.objects.filter(email=request.session['email'])
        print(orders)
        print(request.session['email'])
        if request.method=="POST":
            if 'remove' in request.POST:
                mn=request.POST.get('remove')
                mname=mn.split(",")
                print("remove")
                re=MedicineOrder.objects.get(medicinename=mname[0],useremail=mname[1],email=request.session['email'])
                re.delete()
                orders=MedicineOrder.objects.filter(email=request.session['email'])
                return render(request,"medorders.html",{'orders':orders,'success':'Successfully Deleted '})
            else:
                HttpResponse("Path")
        return render(request,"medorders.html",{'orders':orders})
    except:
        return render(request,"medorders.html")
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

def MedProfilePage(request):
    pro=CheckProfession(request)
    if pro=='patient':
        return redirect('cushome')
    elif pro=='doctor':
        return redirect('dochome')
    doct=Pharmacy.objects.get(email=request.session['email'])
    if request.method=="POST" and "update" in request.POST:
        m=request.POST['mobile']
        mob=""
        print("hello")
        if(len(m)==10):
            mob=request.POST['mobile']
        else:
            mob=request.session['mobile']
        if(request.POST['oldpass']!="" and request.POST['oldpass']!=doct.password):
            return render(request,'medprofile.html',{'profile':doct,'errorp':'incorrect password'})
        if(request.POST['newpass']!="" and request.POST['newpass']!=request.POST['confirmpass']):
            return render(request,'medprofile.html',{'profile':doct,'errorcon':'password wasnot matched'})
        if(request.POST['newpass']==""):
            password=doct.password
        else:
            password=request.POST['newpass']
        request.session['username']=request.POST['username']
        request.session['mobile']=mob
        doct=Pharmacy.objects.filter(email=request.session['email'])
        doct.update(username=request.POST['username'],shopname=request.POST['shopname'],mobile=mob,address=request.POST['address'],password=password)
        doct=Pharmacy.objects.get(email=request.session['email'])
        return render(request,'medprofile.html',{'profile':doct,'success':'successfully updated the data'})
    return render(request,'medprofile.html',{'profile':doct})


def pharmacyUpdateProfilePic(request):
    try:
        u = Pharmacy.objects.get(email=request.session['email'])
        u.profilepic = request.FILES['profilepic']
        u.save()
        return redirect('medprofile')
    except:
        return redirect('login')




# code='''
#     <h1>Hello Sree Krishna</h1>
# '''



# from django.core.mail import send_mail
# def emai():
#     send_mail('sub', code,
#               'imranirfanalikhan786@gmail.com', ['maremandasreekrishna@gmail.com'], fail_silently=False)