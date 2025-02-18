from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .models import Catagory, Post,Contact


class ContactForm(forms.ModelForm):
    name = forms.CharField(label="Name",max_length=30,required=True)
    email = forms.EmailField(label="Email",required=True)
    message = forms.CharField(label="message",max_length=300,required=True)

    class Meta:
        model = Contact
        fields = ['name','email','message']


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

        if not User.objects.filter(email = email).exists:

            raise forms.ValidationError("Invalid email")
        

class ResetPasswordForm(forms.Form):
    new_password = forms.CharField(max_length=20,label="New password",required=True)
    confirm_password = forms.CharField(max_length=20,label="Confirm password",required=True)

    def clean(self):
        cleaned_data = super().clean()
        new_password = cleaned_data.get('new_password')
        confirm_password = cleaned_data.get('confirm_password')

        if new_password and confirm_password and new_password != confirm_password:
            raise forms.ValidationError("Password Doesn't match")
        


class NewPostForms(forms.ModelForm):
    title = forms.CharField(max_length=100,required=True)
    content = forms.CharField(required=True,max_length=3000)
    
    catagory = forms.ModelChoiceField(required=True,queryset=Catagory.objects.all())
    image = forms.ImageField(required=False) 
    class Meta:
        model = Post

        fields = ['title','content','catagory','image']

    def save(self, commit = ...):
        post = super().save(commit)
        cleaned_data = super().clean()
        if cleaned_data.get('image'):
            post.image = cleaned_data.get('image')
        else:
            image = "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg?20200913095930"
            post.image = image
        if commit:
            post.save()
        return post


