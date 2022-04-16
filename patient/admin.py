from django.contrib import admin

# Register your models here.
from .models import Patient,Hospital, Appointment, MedicineCart

admin.site.register(Patient)
admin.site.register(Hospital)
admin.site.register(Appointment)
admin.site.register(MedicineCart)