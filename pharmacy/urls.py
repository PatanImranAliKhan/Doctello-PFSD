from django.urls import path
from . import views

urlpatterns = [
    path('',views.PharmacyHomePage,name="pharmacyhome"),
    path('contact/',views.ContactPage,name="medcontact"),
    path('about/',views.AboutPage,name="medabout"),
    path('addmedicines/',views.AddMedicinePage,name="addmedicine"),
    path('Orders/',views.OrdersPage,name="medicineorders"),
    path('allmedicines/',views.AllMedicinesPage,name="allmedicines"),
    path('logout/',views.LogoutDoctello,name="medlogout"),
    path('profile/',views.MedProfilePage,name="medprofile"),
    path('update_profile/',views.pharmacyUpdateProfilePic,name="medupdateprofile")
]