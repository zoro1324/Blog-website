from django.shortcuts import render,redirect,get_object_or_404
from django.urls import reverse
from django.http import Http404
from .models import Catagory, Post,AboutUs
from django.core.paginator import Paginator
from .forms import ContactForm,RegisterForm,LoginForm,ForgotPasswordForm,ResetPasswordForm,NewPostForms
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.models import User,Group
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required,permission_required
from django.utils.safestring import mark_safe

# Create your views here.

def rediret_to_index(request):
    return redirect(reverse("blog:index"))

def index(request):

    search = request.GET.get('query','')
    if search:
        
        posts = Post.objects.filter(is_published = True,title__icontains = search)
        if not posts:
            messages.warning(request,"No such Post Exist")
            print("IF")

    else:
        posts = Post.objects.filter(is_published = True)
        
        
    paginator = Paginator(posts,6)
    page_num = request.GET.get("page")
    page_obj = paginator.get_page(page_num)
    return render(request,"blog/index.html",{"title":"Home Page","page_obj":page_obj})

def detail(request,slug):
    try:
        data = Post.objects.get(slug=slug)
        related_posts = Post.objects.filter(catagory = data.catagory )
    except Post.DoesNotExist:
        raise Http404("Page does not exist")
    return render(request,"blog/detail.html",{"post":data,"related_posts":related_posts,'not_bottom':True})


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        if form.is_valid():
            form.save()
            messages.success(request,"Your resonse has been recorded!")
            return render(request,"blog/contact.html")
        return render(request,"blog/contact.html",{"form":form,"name":name,"email":email,"message":message})
    
    return render(request,"blog/contact.html",{"title":"Contact Us"})


def about(request):
    data = AboutUs.objects.first()
    content = data.content
    
    safe_data = mark_safe(content)
    return render(request,"blog/aboutus.html",{"content":safe_data,"title":"About Us","image":data.formeted_image,'not_bottom':True})


def register(request):
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user_data = form.save(commit=False)
            user_data.set_password(form.cleaned_data["password"])
            user_data.save()
            writer,created = Group.objects.get_or_create(name = "Editor")
            user_data.groups.add(writer)
            messages.success(request,"Registeration Successful, Now you can login")
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

@login_required
def dashboard(request):

    posts = Post.objects.filter(user = request.user)
    paginator = Paginator(posts,3)
    current_page  = request.GET.get('page')
    page_obj = paginator.get_page(current_page)
    return render(request,"blog/dashboard.html",{"title":"Dashboard","page_obj":page_obj,'user':request.user})


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
            messages.success(request,"Verification Email has been sent your mail")
    return render(request,"blog/forgotpassword.html",{'title':"Forgot Password","form":form})



def resetpassword(request,uidb64,token):
    form = ResetPasswordForm()
    if request.method == "POST":
        form = ResetPasswordForm(request.POST)
        
        if form.is_valid():
            new_pass = form.cleaned_data['new_password']
            try:
                pk = urlsafe_base64_decode(uidb64)
                user = User.objects.get(pk=pk)
            except:
                user = None

            if user is not None and default_token_generator.check_token(user,token):
                user.set_password(new_pass)
                user.save()
                messages.success(request,"Your password has been successfully updated.")
            else:
                messages.error(request,"Your redirect link has been expired")

    return render(request,"blog/resetpassword.html",{"title":"Reset password",'form':form})


@login_required
@permission_required('blog.add_post',raise_exception=True)
def newpost(request):
    form = NewPostForms()
    catagories = Catagory.objects.all()
    if request.method == "POST":
        form = NewPostForms(request.POST, request.FILES)
        
        
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            messages.success(request,"New Post has been created.")
            return redirect(reverse('blog:dashboard'))
    return render(request,"blog/newpost.html",{'title':'New Post','catagories':catagories,'form':form})

@login_required
@permission_required("blog.change_post",raise_exception=True)
def editpost(request,slug):
    catagories = Catagory.objects.all()
    post = get_object_or_404(Post,slug=slug)
    form = NewPostForms()
    if request.method == 'POST':
        form = NewPostForms(request.POST,request.FILES,instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            messages.success(request,"Post has been updated!")
            return redirect(reverse("blog:dashboard"))
    return render(request,"blog/editpost.html",{"post":post,"catagories":catagories,"form":form,'title':'Edit Post'})

@login_required
@permission_required('blog.delete_post',raise_exception=True)
def deletepost(request,slug):
    post = get_object_or_404(Post,slug=slug)
    post.delete()
    return redirect(reverse('blog:dashboard'))

@permission_required("blog.publish_post")
@login_required
def publishpost(request,slug):
    post = get_object_or_404(Post,slug = slug)
    post.is_published = True
    post.save()
    messages.success(request,"Post has been Published.")
    return redirect(reverse("blog:dashboard"))

def search_post(request):
    pass