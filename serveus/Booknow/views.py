from django.shortcuts import render
from django.http import HttpResponse
from .models import customer,service_providers
import json


def index(request):
	return render(request, 'Booknow/index.html')

def logUser(request):
	return render(request, 'Booknow/login.html')

def logsp(request):
	return render(request, 'Booknow/loginSP.html')

def signUpUser(request):
	return render(request, 'Booknow/regCus.html')

def signUpSP(request):
	return render(request, 'Booknow/regSP.html')

def verLogUser(request):
    if request.method == 'POST':
        canEmail = request.POST.get('usrEmail','')
        canPass = request.POST.get('usrPass','')
        print(canPass)
        candi = customer.objects.get(C_email=canEmail);
        if (candi):
            if (candi.C_password == canPass):
                print("password is correct")
                response_data = {}
                response_data['replyBot'] = "success"
                # request.session['username'] = canEmail
                return HttpResponse(
                    json.dumps(response_data),
                    content_type="application/json"
                )

def verLogSP(request):
    if request.method == 'POST':
        canEmail = request.POST.get('usrEmail','')
        canPass = request.POST.get('usrPass','')
        print(canPass)
        candi = service_providers.get(SPemail=canEmail)
        if (candi):
            if (candi.SPpassword == canPass):
                print("Password is correct")
                response_data = {}
                response_data['replyBot'] = "success"
                # request.session['username'] = canEmail
                return HttpResponse(
                    json.dumps(response_data),
                    content_type="application/json"
                )


def regisCus(request):
    if request.method == 'POST':
        canEmail = request.POST.get('usrEmail','')
        canPass = request.POST.get('usrPass','')
        canName = request.POST.get('usrName','')
        canAddress = request.POST.get('usrAddress','')
        canPhone = request.POST.get('usrPh','')
        canConfirm = request.POST.get('usrConPass','')
        # cus = customer(C_Name=canName,C_Phone_num='077',C_Address='COlombo',C_email=canEmail,C_Password=canPass,C_rating=0)
        # if(canPhone == canConfirm):
        cus = customer()
        cus.C_Name = canName
        cus.C_email = canEmail
        cus.C_password = canPass
        cus.C_Phone_num = canPhone
        cus.C_Address=canAddress
        cus.save()
        response_data = {}
        response_data['replyBot'] = "success"
        request.session['username'] = canEmail
        return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )

def regisSP(request):
    if request.method == 'POST':
        SPEmail = request.POST.get('usrEmail', '')
        SPPass = request.POST.get('usrPass', '')
        SPName = request.POST.get('usrName', '')
        SPAddress = request.POST.get('usrAddress', '')
        SPPhone = request.POST.get('usrPh', '')
        SPConfirm = request.POST.get('usrConPass', '')
        # cus = customer(C_Name=canName,C_Phone_num='077',C_Address='COlombo',C_email=canEmail,C_Password=canPass,C_rating=0)
        # if(canPhone == canConfirm):
        cus = customer()
        cus.C_Name = SPName
        cus.C_email = SPEmail
        cus.C_password = SPPass
        cus.C_Phone_num = SPPhone
        cus.C_Address = SPAddress
        cus.save()
        response_data = {}
        response_data['replyBot'] = "success"
        request.session['username'] = SPEmail
        return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )
