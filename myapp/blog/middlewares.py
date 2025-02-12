
from django.urls import reverse
from django.shortcuts import redirect

class RedirectAuthUserMiddleware:

    def __init__(self,get_response):

        self.get_response = get_response

    def __call__(self,request):
        
        

        if request.user.is_authenticated:
            invalid_urls = [reverse("blog:login"),reverse("blog:register")]
            if request.path in invalid_urls:

                return redirect(reverse('blog:index'))
            
        response = self.get_response(request)

        return response
    

class RedirectNonAuthUser:

    def __init__(self,get_response):
        self.get_response = get_response

    def __call__(self,request):
        invalid_urls = [reverse("blog:dashboard"),reverse("blog:logout")]

        if not request.user.is_authenticated:
            if request.path in invalid_urls:
                return redirect(reverse("blog:login"))
        
        response = self.get_response(request)

        return response