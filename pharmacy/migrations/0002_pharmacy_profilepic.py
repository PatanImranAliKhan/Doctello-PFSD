# Generated by Django 4.0.4 on 2022-04-16 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pharmacy', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pharmacy',
            name='profilepic',
            field=models.ImageField(default='profilepics\\defaultpicimg.png', upload_to='profilepics/'),
        ),
    ]
