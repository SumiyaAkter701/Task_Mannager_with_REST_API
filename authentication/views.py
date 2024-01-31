
from django.shortcuts import render,redirect,HttpResponse,get_object_or_404
from .form import SignUp_From, SignIn_Form
from django.contrib.auth import authenticate,login,logout
from .models import CustomUser
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponseRedirect
from django.contrib import messages
import random

# Create your views here.

def sign_up(request):
    form = SignUp_From()
    if request.user.is_authenticated:
        return redirect('sign_in')
    if request.method == 'POST':
        form  = SignUp_From(request.POST)
        if form.is_valid():
            user = form .save() 
            password = form .cleaned_data['password1']
            user.set_password(password)
            user.save()
            return redirect('sign_in')
        else:
            return HttpResponse(form.errors)
        
    return render(request,'authentication/sign_up.html',{'form':form})

def sign_in(request):
    if request.method=="POST":
        form=SignIn_Form(request.POST)
        if form.is_valid():
            
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            
            user = authenticate(request, username=username, password=password)
            if not user:
                messages.warning(request,'The User Account not found')
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            
            if user:
                
                login(request, user)
                return redirect("task_list")
    else:
        form=SignIn_Form()
    
    return render(request,'authentication/sign_in.html',{'form':form})

def sign_out(request):
    logout(request)
    return redirect('sign_in')

def forget_password(request):
    if request.user.is_authenticated:
        return redirect('task_list')
    
    if request.method == 'POST':
        otp = random.randint(111111, 999999)
        email = request.POST['email']
        if CustomUser.objects.filter(email=email).exists():
            user = get_object_or_404(CustomUser, email=email)
            user.otp = otp
            user.save()
            
            subject = "OTP Verificatino For Forget Password!"
            message = f"""Dear User,
            Your OTP is: {otp}
            """
            from_email = settings.EMAIL_HOST_USER
            recipient_list = [email]
            send_mail(subject, message, from_email, recipient_list)
            
            return render(request,'authentication/reset_password.html', {'email': email})
        
        else:
            messages.warning(request, 'Email Address Does Not Exists!')
            return redirect(request.META['HTTP_REFERER'])

    return render(request,'authentication/forget_pass.html')

def reset_password(request):
    if request.user.is_authenticated:
        return redirect('task_list')
    
    if request.method == 'POST':
        email = request.POST['email']
        otp = request.POST['otp']
        password = request.POST['password']
        
        user = get_object_or_404(CustomUser, email=email)
        if user.otp != otp:
            messages.warning(request, 'Wrong OTP!')
            return redirect(request.META['HTTP_REFERER'])
        
        user.set_password(password)
        user.save()
        messages.success(request, 'Password Reset Successfully!')
        return redirect('sign_in')
    
    return render(request,'authentication/reset_password.html') 


