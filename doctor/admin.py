from django.contrib import admin

# Register your models here.
from .models import Doctor, HealthTips, Slot, Consult

admin.site.register(Doctor)
admin.site.register(HealthTips)
admin.site.register(Slot)
admin.site.register(Consult)