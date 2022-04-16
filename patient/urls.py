from os import name
from django.urls import path
from . import views

urlpatterns = [
    path('',views.PatientHome,name="patient_home"),
    path('orders/',views.patient_Orders,name="patient_orders"),
    path('cart/',views.patient_cart,name="patient_cart"),
    path('hospitals/',views.HospitalsList,name="hospitalslist"),
    path('payment/',views.Payment,name="payment"),
    path('consults/',views.ConsultsPage,name="consult"),
    path('consultDoctor/<email>/<date>',views.ConsultDoctor,name="consultdoctor"),
    path('updateconsultDoctor/',views.UpdateProbleToConsultation,name="updateconsultdoctor"),
    path('contact/',views.ContactPage,name="patient_contact"),
    path('about/',views.AboutPage,name="patient_about"),
    path('appointment/<str:name>',views.Appointmentpage,name="appointment"),
    path('logout/',views.LogoutDoctello,name="patient_logout"),
    path('medicines/',views.MedicinesPage,name="medicines"),
    path('healthtips/',views.HealthTipsPage,name="patient_healthtips"),
    path('profile',views.ProfilePage,name="patient_profile"),
    path('update_profile/',views.patientUpdateProfilePic,name="patient_update_profile"),
    path('allconsultations/',views.AllconsultationsPage,name="allconsultations"),
    path('placeorder/',views.Placeorder,name="placeorder")
]