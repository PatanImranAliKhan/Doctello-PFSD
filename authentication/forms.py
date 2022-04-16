from django import forms
from patient.models import Patient
from doctor.models import Doctor
from pharmacy.models import Pharmacy
from django.forms import TextInput, PasswordInput,NumberInput,EmailInput, FileInput, IntegerField
from .models import Feedback


class PatientForm(forms.ModelForm):
    class Meta:
        model=Patient
        fields= ['firstname','lastname','email','mobile','location','address','password','agreement']
        widgets={
            'firstname': TextInput(attrs={'type':'text','placeholder':'First Name','class':'form-control','name':'firstname'}),
            'lastname': TextInput(attrs={'type':'text','placeholder':'Last Name','class':'form-control','name':'lastname'}),
            'email': EmailInput(attrs={'type':'email','placeholder':'example@gmail.com','class':'form-control','name':'email'}),
            'mobile': NumberInput(attrs={'type':'tel','placeholder':'PhoneNumber','class':'form-control','name':'mobile'}),
            'location': forms.Select(attrs={'type':'text','placeholder':'Location','class':'form-control','name':'location'}),
            'address': TextInput(attrs={'type':'text','placeholder':'Address','class':'form-control','name':'address'}),
            'password': PasswordInput(attrs={'type':'password','placeholder':'Password','class':'form-control','name':'password'}),
            'agreement':forms.CheckboxInput(attrs={'type':'checkbox','name':'agreement'})
        }

class DoctorForm(forms.ModelForm):
    class Meta:
        model=Doctor
        fields=['firstname','lastname','email','mobile','location','qualification','specialization','experience','consultationfee','resume','idproof','description','password','agreement']
        widgets={
            'firstname':TextInput(attrs={'type':'text','placeholder':'First Name','class':'form-control','name':'firstname'}),
            'lastname':TextInput(attrs={'type':'text','placeholder':'Last Name','class':'form-control','name':'lastname'}),
            'email':EmailInput(attrs={'type':'email','placeholder':'example@gmail.com','class':'form-control','name':'email'}),
            'mobile': NumberInput(attrs={'type':'tel','placeholder':'PhoneNumber','class':'form-control','name':'mobile'}),
            'location':forms.Select(attrs={'type':'text','placeholder':'Location','class':'form-control','name':'location'}),
            'qualification':TextInput(attrs={'type':'text','placeholder':'qualification','class':'form-control','name':'qualification'}),
            'specialization':forms.Select(attrs={'type':'text','placeholder':'specialization','class':'form-control','name':'specialization'}),
            'experience':NumberInput(attrs={'type':'number','placeholder':'Experience','class':'form-control','name':'experience'}),
            'consultationfee':NumberInput(attrs={'type':'number','placeholder':'Consult Fee','class':'form-control','name':'consultationfee'}),
            'resume':FileInput(attrs={'type':'file','accept':'application/pdf,application/jpg,application/png','class':'form-control','name':'resume'}),
            'idproof':FileInput(attrs={'type':'file','accept':'application/pdf,application/jpg,application/png','class':'form-control','name':'idproof'}),
            'description':forms.Textarea(attrs={'type':'text','placeholder':'Describe why your are joining in this...','class':'form-control','name':'description','rows':"3"}),
            'password':forms.PasswordInput(attrs={'type':'password','placeholder':'Password','class':'form-control','name':'password'}),
            'agreement':forms.CheckboxInput(attrs={'type':'checkbox','name':'agreement'})
        }

class PharmacyForm(forms.ModelForm):
    class Meta:
        model=Pharmacy
        fields=['username','shopname','email','mobile','location','experience','deliverycharge','address','resume','shopproofs','password','agreement']
        widgets={
            'username':TextInput(attrs={'type':'text','placeholder':'Username','class':'form-control','name':'username'}),
            'shopname':TextInput(attrs={'type':'text','placeholder':'Shopname','class':'form-control','name':'shopname'}),
            'email':EmailInput(attrs={'type':'email','placeholder':'example@gmail.com','class':'form-control','name':'email'}),
            'mobile': NumberInput(attrs={'type':'tel','placeholder':'PhoneNumber','class':'form-control','name':'mobile'}),
            'location':forms.Select(attrs={'type':'text','placeholder':'Location','class':'form-control','name':'location'}),
            'experience':NumberInput(attrs={'type':'number','placeholder':'Experience','class':'form-control','name':'experience'}),
            'deliverycharge':NumberInput(attrs={'type':'number','placeholder':'Delivery Charge Fee','class':'form-control','name':'deliverycharge'}),
            'address': TextInput(attrs={'type':'text','placeholder':'Shop Address','class':'form-control','name':'address'}),
            'resume':FileInput(attrs={'type':'file','accept':'application/pdf,application/jpg,application/png','class':'form-control','name':'resume'}),
            'shopproofs':FileInput(attrs={'type':'file','accept':'application/pdf,application/jpg,application/png','class':'form-control','name':'shopproofs'}),
            'password':forms.PasswordInput(attrs={'type':'password','placeholder':'Password','class':'form-control','name':'password'}),
            'agreement':forms.CheckboxInput(attrs={'type':'checkbox','name':'agreement'})
        }

class LoginForm(forms.Form):
    email=forms.CharField(widget=forms.EmailInput(attrs={'type':'email','placeholder':'example@gmail.com','class':'form-control','name':'email'}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={'type':'password','placeholder':'Password','class':'form-control','name':'password'}))


class FeedbackForm(forms.ModelForm):
    class Meta:
        model=Feedback
        fields='__all__'
        widgets={
            'name':TextInput(attrs={'type':'text','placeholder':'Username','class':'form-control form-control-md','name':'name'}),
            'email':EmailInput(attrs={'type':'email','placeholder':'example@gmail.com','class':'form-control form-control-md','name':'email'}),
            'mobile': NumberInput(attrs={'type':'tel','placeholder':'PhoneNumber','class':'form-control form-control-md','name':'mobile'}),
            'feedback':forms.Textarea(attrs={'type':'text','placeholder':'Enter your Feedback...','class':'form-control form-control-md','name':'feedback','rows':'5'}),
        }