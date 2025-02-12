from django.shortcuts import render,redirect
from django.urls import reverse
from django.http import Http404
from .models import Post,AboutUs
from django.core.paginator import Paginator
from .forms import ContactForm,RegisterForm,LoginForm,ForgotPasswordForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.core.mail import send_mail

# Create your views here.

def rediret_to_index(request):
    return redirect(reverse("blog:index"))

def index(request):
    posts = Post.objects.all()
    paginator = Paginator(posts,9)
    page_num = request.GET.get("page")
    page_obj = paginator.get_page(page_num)
    

    return render(request,"blog/index.html",{"title":"Home Page","page_obj":page_obj})

def detail(request,slug):
    try:
        data = Post.objects.get(slug=slug)
        related_posts = Post.objects.filter(catagory = data.catagory )
    except Post.DoesNotExist:
        raise Http404("Page does not exist")
    return render(request,"blog/detail.html",{"post":data,"related_posts":related_posts})


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        if form.is_valid():
            valid_form = True
            return render(request,"blog/contact.html",{"valid_form":valid_form})
        return render(request,"blog/contact.html",{"form":form,"name":name,"email":email,"message":message})
    
    return render(request,"blog/contact.html",{"title":"Contact Us"})


def about(request):
    data = AboutUs.objects.first()
    return render(request,"blog/aboutus.html",{"data":data,"title":"About Us"})


def register(request):
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user_data = form.save(commit=False)
            user_data.set_password(form.cleaned_data["password"])
            user_data.save()
            messages.success(request,"Registeration Successful now you can log in")
            return redirect(reverse("blog:login"))
            
    return render(request,"blog/register.html",{"title":"Register User","form":form})


def login_view(request):

    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        
        if form.is_valid():
            
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username,password=password)

            if user is not None:
                login(request,user)
                return redirect(reverse("blog:dashboard"))

    return render(request,"blog/login.html",{"title":"Log in","form":form})


def dashboard(request):
    return render(request,"blog/dashboard.html",{"title":"Dashboard"})


def logout_view(request):
    logout(request)
    return redirect("blog:index")


def forgotpassword(request):

    form = ForgotPasswordForm()

    if request.method == 'POST':

        form = ForgotPasswordForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data['email']
            user = User.objects.get(email=email)
            subject = "Password Change request"
            current_site = get_current_site(request)
            
            domain = current_site.domain
            token = default_token_generator.make_token(user)
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            message = render_to_string("blog/email.html",{"domain":domain,"uid":uid,"token":token})
            
            send_mail(subject,message,"noreply@zoro.com",[email])
            messages.success(request,"Email sent")
    return render(request,"blog/forgotpassword.html",{'title':"Forgot Password","form":form})


def resetpassword(request):
    pass