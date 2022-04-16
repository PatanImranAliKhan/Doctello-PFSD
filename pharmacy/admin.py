from django.contrib import admin

# Register your models here.
from .models import Pharmacy, Medicine, MedicineOrder

admin.site.register(Pharmacy)
admin.site.register(Medicine)
admin.site.register(MedicineOrder)