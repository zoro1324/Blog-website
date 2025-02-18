from django.shortcuts import render

def coustom_page_not_found(request,exception):
    return render(request,"404.html",status=404)

def page_403(request,exception):
    return render(request,'403.html',status=403)

