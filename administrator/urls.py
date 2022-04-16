from django.urls import path

from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns =[
    path('',views.AdminHomePage,name="adminhome"),
    path('pie-chart/', views.pie_chart, name='pie-chart'),
    path('newdoctors/', views.ViewnewDoctors, name='newdoctors'),
    path('newpharmacy/', views.viewnewPharmacy, name='newpharmacy'),
    path('doctordetails/<email>/', views.DoctorDetails, name='doctordetails'),
    path('pharmacydetails/<email>/', views.PharmacyDetails, name='pharmacydetails'),
    path('displaypdf/<filename>/', views.DisplayPDFData, name='displaypdf'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)