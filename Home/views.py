from django.shortcuts import render, redirect
from django.urls import reverse

from .forms import RegisterForm
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .forms import *
from .models import *

# Create your views here.

def index(request):
    return render(request, 'home/index.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            messages.success(request, "Login Successfull")
            return redirect('dashboard_user')
        else:
            messages.success(request,"Either password or username is incorrect...")
            return redirect('home')

    return render(request, 'home/login.html')

def user_register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            #authencitate
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username= username, password=password)
            login(request, user)
            messages.success(request, "Login Successfull")
            return redirect ('dashboard_user') 
    else:
        form = RegisterForm()    
        return render(request, 'home/register.html',{'form':form})
       
    return render(request, 'home/register.html',{'form':form})


def user_logout(request):
    logout(request)
    messages.success(request, "Successfully Logout....")
    return redirect("home")


def user_dashboard(request):
    return render(request,'users/dashboard.html')

def image_display(request):
    image_url = "{% statics 'porsche.png' %}"  # Replace this with the actual URL of your image
    num_times = 5  # Number of times to display the image
    return render(request, 'index.html', {'image_url': image_url, 'num_times': num_times})

def site_setting(request):
    return render(request, 'users/site_setting.html')

def user_blank(request):
    return render(request, 'users/user_blank.html')

def user_pages(request):
    return render(request, 'users/user_pages.html')

def submit_user_info(request):
        user_id = request.user.id
        about = request.POST.get('about')
        company = request.POST.get('company')
        job = request.POST.get('job')
        country = request.POST.get('country')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        fb_profile = request.POST.get('facebook')
        inst_profile = request.POST.get('instagram')
        link_profile = request.POST.get('linkedin')
        tw_profile = request.POST.get('twitter')
        
        #store in auth_user table
        fullName = request.POST['fullName']
        email = request.POST['email']
        names = fullName.split(' ')
        first_name = names[0]
        last_name = names[1]
        
        if first_name and last_name and email:
            find_user = User.objects.filter(pk=user_id)
            find_user.update(first_name=first_name,last_name=last_name, email=email)
        
        # Validate and save the data in userinfo table
        print("this is user id")
        print(user_id)
        if user_id and company and about and job and country and address and phone and fb_profile and inst_profile and link_profile and tw_profile:
            user_info = UserInfo(user=User.objects.get(pk=user_id),company=company, about=about, job=job, country=country, address=address, phone=phone, fb_profile=fb_profile, inst_profile=inst_profile, link_profile=link_profile, tw_profile=tw_profile)
            user_info.save()
            print("success")
            return 1
        print("Error")
        return 0; 

def user_profile(request):
    user_info = UserInfo.objects.get(user_id=request.user.id)
    if request.method == 'POST':
        asd = submit_user_info(request)
        if(asd == 1):
            messages.success(request, "Profile Updated Successfully", extra_tags="profile_success")
            return redirect(reverse('user_profile'))
        else:
            messages.success(request, "Something Went Wrong Please Check..", extra_tags="profile_success")
            return redirect(reverse('user_profile'))
        
    return render(request, 'users/user_profile.html',{'user_info':user_info})


def edit_profile(request):  
    if request.method == 'POST':
        print('post method')
        
        user_info = UserInfo.objects.get(user_id=request.user.id) 
        print(user_info.about)
        user_info.about = request.POST.get('about')
        user_info.job = request.POST.get('job')
        user_info.country = request.POST.get('country')
        user_info.address = request.POST.get('address')
        user_info.phone = request.POST.get('phone')
        user_info.fb_profile = request.POST.get('fb_profile')
        user_info.inst_profile = request.POST.get('inst_profile')
        user_info.link_profile = request.POST.get('link_profile')
        user_info.tw_profile = request.POST.get('tw_profile')
        user_info.company = request.POST.get('company')
        
        print(user_info)
        
        user_info.save()
    
    print('get request')
    return redirect('user_profile')

def user_table(request):
    return render(request, 'users/user_table.html')
