from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('register/patient/',views.PatientReg,name="patientReg"),
    path('register/doctor/',views.DoctorReg,name="doctorReg"),
    path('register/pharmacy/',views.PharmacyReg,name="pharmacyReg"),
    path('login/',views.LoginDoctello,name="login"),
    path('register/',views.RegisterPage,name="register"),
    path('logout/',views.LogoutDoctello,name="logout"),
]