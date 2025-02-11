from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label="Name",max_length=30,required=True)
    email = forms.EmailField(label="Email",required=True)
    message = forms.CharField(label="message",max_length=300,required=True)