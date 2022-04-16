from django.db import models

# Create your models here.

class Feedback(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    mobile=models.BigIntegerField()
    feedback=models.CharField(max_length=300)