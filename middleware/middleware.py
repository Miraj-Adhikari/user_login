from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import redirect
from django.urls import reverse


class usermiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        
        
    def __call__(self, request):
        if request.user.is_authenticated and request.path.startswith('/login/') or request.path.startswith('/register/'):
            return redirect('/user/dashboard')
            
        if request.path.startswith('/user/'):
            if not request.user.is_authenticated:
                return redirect(reverse('login_page'))  # Redirect to login if not authenticated
            
        response = self.get_response(request)
        return response