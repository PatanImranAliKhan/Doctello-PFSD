# Generated by Django 4.0.4 on 2022-04-16 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Consult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('useremail', models.EmailField(max_length=100)),
                ('doctorname', models.CharField(default='', max_length=100)),
                ('doctoremail', models.EmailField(max_length=100)),
                ('date', models.DateField()),
                ('slot', models.CharField(choices=[('9:00am - 10:30am', '9:00am - 10:30am'), ('11:00am - 12:30pm', '11:00am - 12:30pm'), ('1:00pm - 2:30pm', '1:00pm - 2:30pm'), ('3:00pm - 4:00pm', '3:00pm - 4:00pm')], default='9:00am - 10:30am', max_length=50)),
                ('report', models.CharField(blank=True, default='', max_length=100)),
                ('problem', models.CharField(default='', max_length=100)),
                ('status', models.CharField(default='', max_length=3000)),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('firstname', models.CharField(max_length=30)),
                ('lastname', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=30, primary_key=True, serialize=False, unique=True)),
                ('mobile', models.BigIntegerField()),
                ('location', models.CharField(choices=[('Anantapur', 'Anantapur'), ('Chittoor', 'Chittoor'), ('East Godavari', 'East Godavari'), ('Guntur', 'Guntur'), ('Kadapa', 'Kadapa'), ('Krishna', 'Krishna'), ('Kurnool', 'Kurnool'), ('Nellore', 'Nellore'), ('Prakasam', 'Prakasam'), ('Srikakulam', 'Srikakulam'), ('Vishakapatnam', 'Vishakapatnam'), ('Viziayanagaram', 'Viziayanagaram'), ('West Godavari', 'West Godavari')], default='Anantapur', max_length=50)),
                ('qualification', models.CharField(max_length=30)),
                ('specialization', models.CharField(choices=[('Allergists/Immunologists', 'Allergists/Immunologists'), ('Anesthesiologists', 'Anesthesiologists'), ('Cardiologists', 'Cardiologists'), ('Colon and Rectal Surgeons', 'Colon and Rectal Surgeons'), ('Dermatologists', 'Dermatologists'), ('Endocrinologists', 'Endocrinologists'), ('Family Physicians', 'Family Physicians'), ('Gastroenterologists', 'Gastroenterologists'), ('Hematologists', 'Hematologists'), ('Infectious Disease Specialists', 'Infectious Disease Specialists'), ('Nephrologists', 'Nephrologists'), ('Neurologists', 'Neurologists'), ('Oncologists', 'Oncologists'), ('Physiatrists', 'Physiatrists')], default='Allergists/Immunologists', max_length=30)),
                ('experience', models.IntegerField()),
                ('consultationfee', models.IntegerField()),
                ('resume', models.FileField(upload_to='doctorResume/')),
                ('idproof', models.FileField(upload_to='doctorproof/')),
                ('description', models.CharField(max_length=500)),
                ('password', models.CharField(max_length=30)),
                ('agreement', models.CharField(max_length=10)),
                ('assign', models.CharField(choices=[('False', 'False'), ('True', 'True')], default='False', max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='HealthTips',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('problem', models.CharField(choices=[('Allergies', 'Allergies'), ('Cold and Flu', 'Cold and Flu'), ('Conjunctivitis (pink eye)', 'Conjunctivitis (pink eye)'), ('Diarrhea', 'Diarrhea'), ('Headache', 'Headache'), ('Mononucleosis', 'Mononucleosis'), ('Stomach Ache', 'Stomach Ache'), ('Nausea and Vomiting', 'Nausea and Vomiting')], default='Allergies', max_length=1000)),
                ('causes', models.CharField(max_length=1000)),
                ('symptoms', models.CharField(max_length=1000)),
                ('prevention', models.CharField(max_length=1000)),
                ('medicine', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Slot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=100)),
                ('location', models.CharField(max_length=50)),
                ('date', models.DateField()),
                ('slot', models.CharField(choices=[('9:00am - 10:30am', '9:00am - 10:30am'), ('11:00am - 12:30pm', '11:00am - 12:30pm'), ('1:00pm - 2:30pm', '1:00pm - 2:30pm'), ('3:00pm - 4:00pm', '3:00pm - 4:00pm')], default='9:00am - 10:30am', max_length=50)),
            ],
        ),
    ]
