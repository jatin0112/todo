from django.shortcuts import redirect, render, HttpResponse
from .forms import CustomSignupForm
from django.core.mail import send_mail
import math, random

# Create your views here.
def signup(request):
    if request.method == "POST":
        signup_form = CustomSignupForm(request.POST)
        if signup_form.is_valid():
            signup_form.save()
            return redirect('reminder')
    else:
        signup_form = CustomSignupForm()
    return render(request, 'signup.html', {'signup_form':signup_form})
