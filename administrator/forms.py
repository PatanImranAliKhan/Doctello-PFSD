from django import forms
from django.forms import widgets
from .models import Message

class ChatBot(forms.ModelForm):
    class Meta:
        model=Message
        fields='__all__'