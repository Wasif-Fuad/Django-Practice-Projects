from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from accounts.models import Profile
from django.contrib import messages
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate , login , logout
def log_in(request):
    
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user_obj = User.objects.filter(username = email)

        if not user_obj.exists():
            messages.warning(request, 'Account not found.')
            return HttpResponseRedirect(request.path_info)


        if not user_obj[0].profile.is_email_varified:
            messages.warning(request, 'Your account is not verified.')
            return HttpResponseRedirect(request.path_info)

        user_obj = authenticate(username = email , password= password)
        if user_obj:
            login(request , user_obj)
            return redirect('/')

        

        messages.warning(request, 'Invalid credentials')
        return HttpResponseRedirect(request.path_info)


    return render(request ,'accounts/login.html')



def register(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        email=request.POST['email']
        password=request.POST['password']
        user_obj = User.objects.filter(email=email)
        if user_obj.exists():
            messages.warning(request,'Email already in use')
            return HttpResponseRedirect(request.path_info)
        new_user=User.objects.create(first_name=first_name,last_name=last_name,email=email,username=email)
        new_user.set_password(password)
        new_user.save()
        messages.success(request, 'An email has been sent on your mail.')
    return render(request,'accounts/register.html')


def activate(request,email_token):
    print('waiting for activation ')
    try:
        
        p = Profile.objects.get(email_token= email_token)
        print('active',p.is_email_varified)
        p.is_email_varified = True
        p.save()
        print('active',p.is_email_varified)
        return redirect(register)
    except Exception as e:
        return HttpResponse(e)   

