from django.db import models
from datetime import date

# from django.http import request

# Create your models here.

Locationchoices=(('Anantapur','Anantapur'),('Chittoor','Chittoor'),('East Godavari','East Godavari'),
                ('Guntur','Guntur'),('Kadapa','Kadapa'),('Krishna','Krishna'),('Kurnool','Kurnool'),
                ('Nellore','Nellore'),('Prakasam','Prakasam'),('Srikakulam','Srikakulam'),('Vishakapatnam','Vishakapatnam'),
                ('Viziayanagaram','Viziayanagaram'),('West Godavari','West Godavari'))

assignchoices=(('False','False'),('True','True'))

class Pharmacy(models.Model):
    username=models.CharField(max_length=30)
    shopname=models.CharField(max_length=30)
    email=models.EmailField(max_length=30,unique=True,blank=False, primary_key=True)
    mobile=models.BigIntegerField()
    location=models.CharField(max_length=50,choices=Locationchoices,default='Anantapur')
    experience=models.IntegerField()
    deliverycharge=models.IntegerField()
    address=models.CharField(max_length=100)
    resume=models.FileField(upload_to ='pharmacyResume/')
    shopproofs=models.FileField(upload_to ='shopproof/')
    password=models.CharField(max_length=30)
    agreement=models.CharField(max_length=10)
    assign=models.CharField(max_length=30,choices=assignchoices,default='False')
    profilepic=models.ImageField(upload_to='profilepics/', default='profilepics\defaultpicimg.png')

def DeliveryCharges(request):
    ph=Pharmacy.objects.get(request.session['email'])
    return int(ph.deliverycharge)

class Medicine(models.Model):
    medicinename=models.CharField(max_length=100)
    email=models.EmailField(max_length=200)
    location=models.CharField(max_length=50)
    startprice=models.FloatField()
    endprice=models.FloatField()
    image=models.CharField(max_length=300)

class MedicineOrder(models.Model):
    username=models.CharField(max_length=100)
    useremail=models.EmailField(max_length=100)
    usermobile=models.BigIntegerField()
    userlocation=models.CharField(max_length=100)
    medicinename=models.CharField(max_length=100)
    email=models.EmailField(max_length=200)
    location=models.CharField(max_length=50)
    startprice=models.FloatField()
    endprice=models.FloatField()
    image=models.CharField(max_length=200)
    date=models.DateField(default=date.today())
