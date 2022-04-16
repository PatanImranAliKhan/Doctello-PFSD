from django.db import models

Locationchoices=(('Anantapur','Anantapur'),('Chittoor','Chittoor'),('East Godavari','East Godavari'),
                ('Guntur','Guntur'),('Kadapa','Kadapa'),('Krishna','Krishna'),('Kurnool','Kurnool'),
                ('Nellore','Nellore'),('Prakasam','Prakasam'),('Srikakulam','Srikakulam'),('Vishakapatnam','Vishakapatnam'),
                ('Viziayanagaram','Viziayanagaram'),('West Godavari','West Godavari'))

problems=(('Allergies','Allergies'),('Cold and Flu','Cold and Flu'),('Conjunctivitis (pink eye)','Conjunctivitis (pink eye)'),('Diarrhea','Diarrhea'),('Headache','Headache'),('Mononucleosis','Mononucleosis'),('Stomach Ache','Stomach Ache'),('Nausea and Vomiting','Nausea and Vomiting'))

class Patient(models.Model):
    firstname=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)
    email=models.EmailField(max_length=30,unique=True,blank=False, primary_key=True)
    mobile=models.BigIntegerField()
    location=models.CharField(max_length=50,choices=Locationchoices,default='Anantapur')
    address=models.CharField(max_length=200,default="")
    password=models.CharField(max_length=30)
    agreement=models.CharField(max_length=10)
    profilepic=models.ImageField(upload_to='profilepics/', default='profilepics\defaultpicimg.png')


class Hospital(models.Model):
    name=models.CharField(max_length=50)
    rating=models.FloatField()
    mobile=models.BigIntegerField()
    address=models.CharField(max_length=200)
    location=models.CharField(max_length=50,choices=Locationchoices,default='Anantapur')
    image=models.CharField(max_length=300)


confirmationchoices=(('email','email'),('phone number','phone number'))
slot=(('morning','morning'),('afternoon','afternoon'))

class Appointment(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    mobile=models.CharField(max_length=10)
    hospital=models.CharField(max_length=100)
    problem=models.CharField(max_length=100,choices=problems,default='Allergies')
    date=models.DateField()
    slot=models.CharField(max_length=50,choices=slot,default='morning')
    report=models.FileField(upload_to ='medicalreport/',blank=True)
    confirmation=models.CharField(max_length=50,choices=confirmationchoices,default='email')

class MedicineCart(models.Model):
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