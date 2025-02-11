from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path("",views.rediret_to_index,name="redired_index"),
    path("home/",views.index,name="index"),
    path("post/<str:slug>/",views.detail,name="detail"),
    path("contact/",views.contact,name="contact"),
    path("about/",views.about,name="aboutus")
]
