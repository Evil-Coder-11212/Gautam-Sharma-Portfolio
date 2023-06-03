from django import forms
from .models import ContactData

class ContactFormData(forms.ModelForm):
    class Meta:
        model = ContactData
        fields = ["full_name", "message", "subject", "email"]