# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404
from login.forms import UserForm, UserProfileInfoForm, D_Form, T_Form
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .forms import C_Form,T_Form
#from django.utils import timezone
from .models import D_Details,C_Details,Trashcan1
from django.contrib import messages
from django.contrib.auth.models import User

'''registration and login view of contractor'''
def Contractor(request):
    registered = False
    if request.method == 'POST':
        user_from = UserForm(data=request.POST)
        profile_form=UserProfileInfoForm(data=request.POST)
        if user_from.is_valid() and profile_form.is_valid():
            user=user_from.save()
            user.set_password(user.password)
            user.save()
            # driv = profile_form.save()
            # driv.user = user
            # driv.save()

            registered=True
            return HttpResponseRedirect(reverse('index'))
        else:
             return HttpResponse("dfghjklkjhgvghj")

    else:
        user_from = UserForm()
        profile_form=UserProfileInfoForm()
        return render(request,'login/registration.html',{'user_form':user_from,'profile_form':profile_form,'registered':registered})

def Driver(request):
    registered = False
    if request.method == 'POST':
        user_from = UserForm(data=request.POST)
        driver_form=D_Form(data=request.POST)
        if user_from.is_valid() and driver_form.is_valid():
            user=user_from.save()
            user.set_password(user.password)
            user.save()
            driver = driver_form.save()
            driver.user = user
            driver.save()
            registered=True
            return HttpResponseRedirect(reverse('index'))
        else:
             return HttpResponse("dfghjklkjhgvghj")

    else:
        user_from = UserForm()
        driver_form=D_Form()
        return render(request,'login/registration.html',{'user_form':user_from,'driver_form':driver_form,'registered':registered})



def contractor_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('special'))
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'login/log.html')


'''registartion of contractor driver and trashcan'''
def Customer(request):
    if request.method == 'POST':
        form1 = C_Form(request.POST)
        if form1.is_valid():
            user1 = form1.save()
            user1.set_password(user1.C_password)
            user1.save()
            return HttpResponseRedirect(reverse('special'))
            #print("Valid")
            #messages.success(request, "Recorded Successfully !!")
            #form1.save()
        else:
            return HttpResponse("ASDFGHJKL")
    else:
        form1 = C_Form()
        return render(request, 'login/form.html', {'form1': form1})

def Driver(request):
    registered = False
    if request.method == 'POST':
        user_from = UserForm(data=request.POST)
        driver_form=D_Form(data=request.POST)
        if user_from.is_valid() and driver_form.is_valid():
            user=user_from.save()
            user.set_password(user.password)
            user.save()
            driver = driver_form.save()
            driver.user = user
            driver.save()
            registered=True
            return HttpResponseRedirect(reverse('special'))
        else:
             return HttpResponse("The user already exists")
    else:
        user_from = UserForm()
        driver_form=D_Form()
        return render(request,'login/registration.html',{'user_form':user_from,'driver_form':driver_form,'registered':registered})



def driver_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user1 = authenticate(username=username, password=password)
        if user1:
            if user1.is_active:
                login(request,user1)
                return HttpResponseRedirect(reverse('ubidots'))
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'login/log1.html', {})

def Trashcan(request):
    if request.method == 'POST':
        form3 = T_Form(request.POST)
        if form3.is_valid():
            form3.save()
            return HttpResponseRedirect(reverse('special'))
        else:
            return HttpResponse(" Zindagi Zhnd hai ")

    form3 = T_Form()
    return render(request, 'login/form.html', {'form3': form3})


def index(request):
    return render(request,'login/index.html')

def map(request):
    User= User.objects.all()
    context = {'User':  User}
    return render(request,'login/form.html',context)

@login_required
def special(request):
#     User = User.objects.all()
#     context = {'User':User}
     return render(request,'login/Map.html')


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def Ubidots(request):
    data = Trashcan1.objects.all()
    context = { 'data': data }
    return render(request,'login/showd.html',context)

def Multi_map(request):
    trash = Trashcan1.objects.all()
    context = {'trash': trash}
    return render(request,'login/Multi_map.html',context)

def Customer_list(request):
    allcustomers = C_Details.objects.all()
    context = {'allcustomers':allcustomers}
    return render(request,'login/list1.html',context)

def Customer_Detail(request,id=None):
    customer = get_object_or_404(C_Details,id=id)
    context={'customer':customer}
    return render(request,'login/C_Details.html',context)


def Driver_list(request):
    alldrivers = D_Details.objects.all()
    context = {'alldrivers': alldrivers}
    return render(request,'login/list2.html',context)

def Driver_Detail(request,id=None):
    driver= get_object_or_404(D_Details,id=id)
    context={'driver':driver}
    return render(request,'login/D_Details.html',context)

def Trashcan_list(request):
    alltrash=Trashcan1.objects.all()
    context= {'alltrash':alltrash}
    return render(request,'login/list3.html',context)

def Trashcan_Detail(request,id=None):
    # customer = C_Details.objects.all()
    trash=get_object_or_404(Trashcan1,id=id)
    context= {'trash':trash,'customer':customer}
    return render(request,'login/T_Details.html',context)

