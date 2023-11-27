from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import UserRegisterForm
# Create your views here.

def index(request):
    return render(request, 'register_login_logout/index.html')

def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created and you can login as {username}')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request,'register_login_logout/register.html', {'form': form})
