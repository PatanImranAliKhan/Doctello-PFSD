from django import forms

from .models import Hospital, Appointment
from doctor.models import Consult

class AppointmentForm(forms.ModelForm):
    class Meta:
        model=Appointment
        fields='__all__'
        widgets={
            'problem':forms.Select(attrs={'type':'text'}),
            'date':forms.DateInput(attrs={'type':'date'}),
            'report': forms.FileInput(attrs={'type':'file','class':'form-control','name':'report'}),
        }

class ConsultationForm(forms.ModelForm):
    class Meta:
        model=Consult
        fields=['username','useremail','doctorname','doctoremail','date','slot','report','problem']
        widgets={
            'problem':forms.TextInput(attrs={'type':'text'}),
            'slot':forms.Select(),
            'date':forms.DateInput(attrs={'type':'date'}),
            'report': forms.FileInput(attrs={'type':'file','name':'report'}),
        }