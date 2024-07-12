from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUPForm
# Create your views here.


def sign_up(request):
    if request.method == 'POST':
        form = SignUPForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:                         
        form = SignUPForm()
    context = {
        'form': form,
    }
    return render(request, 'users/sign_up.html', context)

def logout(request):
    return render(request, 'users/logout.html')

def profile(request):
    return render(request, 'users/profile.html')
