import time
from django.db import models

Locationchoices=(('Anantapur','Anantapur'),('Chittoor','Chittoor'),('East Godavari','East Godavari'),
                ('Guntur','Guntur'),('Kadapa','Kadapa'),('Krishna','Krishna'),('Kurnool','Kurnool'),
                ('Nellore','Nellore'),('Prakasam','Prakasam'),('Srikakulam','Srikakulam'),('Vishakapatnam','Vishakapatnam'),
                ('Viziayanagaram','Viziayanagaram'),('West Godavari','West Godavari'))

problems=(('Allergies','Allergies'),('Cold and Flu','Cold and Flu'),('Conjunctivitis (pink eye)','Conjunctivitis (pink eye)'),
            ('Diarrhea','Diarrhea'),('Headache','Headache'),('Mononucleosis','Mononucleosis'),('Stomach Ache','Stomach Ache'),
            ('Nausea and Vomiting','Nausea and Vomiting'))

doctorSpecializations=(('Allergists/Immunologists','Allergists/Immunologists'),('Anesthesiologists','Anesthesiologists'),
                        ('Cardiologists','Cardiologists'),('Colon and Rectal Surgeons','Colon and Rectal Surgeons'),
                        ('Dermatologists','Dermatologists'),('Endocrinologists','Endocrinologists'),('Family Physicians','Family Physicians'),
                        ('Gastroenterologists','Gastroenterologists'),('Hematologists','Hematologists'),('Infectious Disease Specialists','Infectious Disease Specialists'),
                        ('Nephrologists','Nephrologists'),('Neurologists','Neurologists'),('Oncologists','Oncologists'),('Physiatrists','Physiatrists'))
                        
# Create your models here.
assignchoices=(('False','False'),('True','True'))
class Doctor(models.Model):
    firstname=models.CharField(max_length=30)
    lastname=models.CharField(max_length=30)
    email=models.EmailField(max_length=30,unique=True,blank=False, primary_key=True)
    mobile=models.BigIntegerField()
    location=models.CharField(max_length=50,choices=Locationchoices,default='Anantapur')
    qualification=models.CharField(max_length=30)
    specialization=models.CharField(max_length=30,choices=doctorSpecializations,default='Allergists/Immunologists')
    experience=models.IntegerField()
    consultationfee=models.IntegerField()
    resume=models.FileField(upload_to ='doctorResume/')
    idproof=models.FileField(upload_to ='doctorproof/')
    description=models.CharField(max_length=500)
    password=models.CharField(max_length=30)
    agreement=models.CharField(max_length=10)
    assign=models.CharField(max_length=30,choices=assignchoices,default='False')
    profilepic=models.ImageField(upload_to='profilepics/', default='profilepics\defaultpicimg.png')


class HealthTips(models.Model):
    problem=models.CharField(max_length=1000,choices=problems,default='Allergies')
    causes=models.CharField(max_length=1000)
    symptoms=models.CharField(max_length=1000)
    prevention=models.CharField(max_length=1000)
    medicine=models.CharField(max_length=1000)

slots=(('9:00am - 10:30am','9:00am - 10:30am'),('11:00am - 12:30pm','11:00am - 12:30pm'),('1:00pm - 2:30pm','1:00pm - 2:30pm'),('3:00pm - 4:00pm','3:00pm - 4:00pm'))
class Slot(models.Model):
    email=models.EmailField(max_length=100)
    location=models.CharField(max_length=50)
    date=models.DateField()
    slot=models.CharField(max_length=50,choices=slots,default='9:00am - 10:30am')

class Consult(models.Model):
    username=models.CharField(max_length=100)
    useremail=models.EmailField(max_length=100)
    doctorname=models.CharField(max_length=100,default="")
    doctoremail=models.EmailField(max_length=100)
    date=models.DateField()
    slot=models.CharField(max_length=50,choices=slots,default="9:00am - 10:30am")
    report=models.CharField(max_length=100,blank=True,default="")
    problem=models.CharField(max_length=100,default="")
    status=models.CharField(max_length=3000,default="")