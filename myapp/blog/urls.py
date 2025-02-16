from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path("",views.rediret_to_index,name="redired_index"),
    path("home/",views.index,name="index"),
    path("post/<str:slug>/",views.detail,name="detail"),
    path("contact/",views.contact,name="contact"),
    path("about/",views.about,name="aboutus"),
    path("register/",views.register,name="register"),
    path("dashboard/",views.dashboard,name="dashboard"),
    path("login/",views.login_view,name="login"),
    path("logout/",views.logout_view,name="logout"),
    path("forgotpassword/",views.forgotpassword,name="forgotpassword"),
    path("resetpassword/<uidb64>/<token>",views.resetpassword,name="resetpassword"),
    path('newpost/',views.newpost,name="newpost")
]
