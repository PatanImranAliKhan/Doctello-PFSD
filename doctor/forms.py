from django import forms
from django.forms import widgets
from .models import HealthTips, Slot, Consult

class HealthTipsForm(forms.ModelForm):
    class Meta:
        model=HealthTips
        fields='__all__'
        widgets={
            'problem': forms.Select(attrs={'class':'form-control form-control-md','type':'text','name':'problem'}),
            'causes': forms.Textarea(attrs={'type':'text','placeholder':'Describe the Causes ...','class':'form-control form-control-md','name':'causes','rows':"5"}),
            'symptoms': forms.Textarea(attrs={'type':'text','placeholder':'Describe the symptoms...','class':'form-control form-control-md','name':'symptoms','rows':"5"}),
            'prevention': forms.Textarea(attrs={'type':'text','placeholder':'preventaions to be taken...','class':'form-control form-control-md','name':'prevention','rows':"5"}),
            'medicine': forms.Textarea(attrs={'type':'text','placeholder':'Medicines used...','class':'form-control form-control-md','name':'medicine','rows':"5"}),
        }

class SlotForm(forms.ModelForm):
    class Meta:
        model=Slot
        fields=['date','slot']
        widgets={
            'date':forms.DateInput(attrs={'type':'date','class':'form-control form-control-md','name':'date'}),
            'slot':forms.Select(attrs={'type':'text','class':'form-control form-control-md','name':'slot'})
        }

class ConsultationForm(forms.ModelForm):
    class Meta:
        model=Consult
        fields='__all__'
        widgets={
            'feedback':forms.Textarea(attrs={'type':'text','placeholder':'Health Status','class':'form-control form-control-md','name':'symptoms','rows':"4"}),
        }