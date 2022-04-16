from django import forms
from .models import Medicine

class MedicineForm(forms.ModelForm):
    class Meta:
        model=Medicine
        fields=['medicinename','startprice','endprice','image']
        widgets={
            'medicinename':forms.TextInput(attrs={'type':'text','class':'form-control form-control-md','name':'medicinename'}),
            'startprice':forms.NumberInput(attrs={'type':'number','class':'form-control form-control-md','name':'startprice'}),
            'endprice':forms.NumberInput(attrs={'type':'number','class':'form-control form-control-md','name':'endprice'}),
            'image':forms.TextInput(attrs={'type':'text','class':'form-control form-control-md','name':'image'})
        }

