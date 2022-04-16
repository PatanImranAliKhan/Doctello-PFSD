from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.DoctorHomePage,name="dochome"),
    path('contact/',views.DocContactPage,name="doccontact"),
    path('about/',views.AboutPage,name="docabout"),
    path('selectslot/',views.SelectSlot,name="selectslot"),
    path('healthtips/',views.TipsPage,name="healthtips"),
    path('slotslist/',views.SlotsListPage,name="slotslist"),
    path('updateslot/<dt>',views.UpdateSlotPage,name="updateslot"),
    path('consults/',views.ConsultsPage,name="consults"),
    path('logout/',views.LogoutDoctello,name="doclogout"),
    path('viewdetails/<name>/<email>/<date>',views.ViewDetails,name="viewdetails"),
    path('profile/',views.DoctorProfilePage,name="doctorprofile"),
    path('update_profile/',views.DoctorUpdateProfilePic,name="doctor_updateprofile")
]