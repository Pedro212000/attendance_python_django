from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.views import View

class HomeView(View):
    def get(self, request):
        return render(request, 'timeAndAttendanceManagement/home.html')

class LoginView(View):
    template_name = 'timeAndAttendanceManagement/login_page.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.is_superuser:  # Only allow superusers
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, "Access denied. Only superusers can log in.")
        else:
            messages.error(request, "Invalid username or password")
        return render(request, self.template_name)
