from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


class ContactForm(forms.Form):
    name = forms.CharField(label="Name",max_length=30,required=True)
    email = forms.EmailField(label="Email",required=True)
    message = forms.CharField(label="message",max_length=300,required=True)


class RegisterForm(forms.ModelForm):
    username = forms.CharField(max_length=20,label="User Name",required=True)
    email = forms.EmailField(label="Email",required=True)
    password = forms.CharField(label="Password",max_length=20,required=True)
    password_confirm = forms.CharField(label="Confirm Password",max_length=20,required=True)

    class Meta:
        model = User
        fields = ["username","email","password"]

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get("password_confirm")

        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError("Password does not match")
        

class LoginForm(forms.Form):
    username = forms.CharField(label="User Name",max_length=20)
    password = forms.CharField(label="Password",max_length=20)

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username,password=password)

            if user is None:
                raise forms.ValidationError("Invalid Username and Password")
            

class ForgotPasswordForm(forms.Form):
    email = forms.EmailField(label="Email",required=True)

    def clean(self):
        cleaned_data = super().clean()

        email = cleaned_data.get("email")

        if User.objects.filter(email = email).exists:
            pass