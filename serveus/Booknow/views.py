from django.shortcuts import render
from django.http import HttpResponse
from django.template.response import TemplateResponse
from .models import customer
from .models import service_list,service_providers
from .models import booking
import json
from datetime import date

# function that loads the main page
def index(request):
	return render(request, 'Booknow/index.html')
#function that
def logUser(request):
	return render(request, 'Booknow/login.html')

def logsp(request):
	return render(request, 'Booknow/login1.html')

def regSP(request):
    return render(request, 'Booknow/signup.html')

def signUpUser(request):
	return render(request, 'Booknow/regCus.html')

def applyBooking(request):
    if request.method == 'POST':
        serveid = request.POST.get('serveid','')
        bookobj = booking.objects.get(id=serveid)
        bookobj.status = "As"
        bookobj.save()
        response_data = {}
        response_data['replyBot'] = "success"
        return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )

def profile(request):
    data = customer.objects.get(C_email=request.session['email'])
    services = service_list.objects.all()
    incomplete = booking.objects.filter(customer_id=data.id,min_price__isnull=False,max_price__isnull=False)
    srch = booking.objects.raw('SELECT b.id,sp.SPName,sp.SPrating,b.description,b.location,b.date_tobe_completed,b.min_price,b.max_price  FROM Booknow_booking b, Booknow_service_providers sp WHERE b.service_provider_id=sp.id AND customer_id=data.id AND min_price>0 AND max_price>0')
    completed = booking.objects.filter(status="C",customer_id=data.id)
    return render(request, 'Booknow/profile-page.html',{"data":data,"services":services,"completed":completed,"incomplete":incomplete,"srch":srch})

def profileSer(request):
    data = service_providers.objects.get(SPemail=request.session['spemail'])
    request.session['SPemail'] = "kasun@gmail.com"
    books = booking.objects.filter(status="TBA")
    completed = booking.objects.filter(status="C",service_provider_id=data.id)
    incomplete = booking.objects.filter(status="As",service_provider_id=data.id)
    return render(request, 'Booknow/profile-page-ser.html',{"data":data,"books":books,"completed":completed,"incomplete":incomplete})

def bidBook(request):
    if request.method == 'POST':
        minprice = request.POST.get('minprice','')
        maxprice = request.POST.get('maxprice','')
        serveid = request.POST.get('servid','')
        print("serveid = "+ serveid)
        bookobj = booking.objects.get(id=serveid)
        bookobj.min_price = minprice
        bookobj.max_price = maxprice
        bookobj.service_provider_id = service_providers.objects.get(SPemail="kasun@gmail.com")
        bookobj.save()
        response_data = {}
        response_data['replyBot'] = "success"
        return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )


def regBook(request):
    if request.method == 'POST':
        serviceType = request.POST.get('serviceType','')
        location = request.POST.get('location','')
        Date1 = request.POST.get('date', '')
        description = request.POST.get('description', '')
        print(serviceType)

        book = booking()
        book.description = description
        book.location = location
        myDate = date.today()
        datestr = str(myDate.year) + "-" + str(myDate.month) + "-" + str(myDate.day)
        book.date_added = datestr
        book.date_tobe_completed = Date1
        book.category_id = service_list.objects.get(type=serviceType).id
        book.customer_id = customer.objects.get(C_email=request.session['email']).id
        book.status = "TBA"
        book.save()
        response_data = {}
        response_data['replyBot'] = "success"
        return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )


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
                request.session['email'] = canEmail
                request.session['name'] = candi.C_Name
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

def rgsp(request):
    if request.method == 'POST':
        canEmail = request.POST.get('usrEmail','')
        canPass = request.POST.get('usrPass','')
        canName = request.POST.get('usrName','')
        canAddress = request.POST.get('usrAddress','')
        canPhone = request.POST.get('usrPh','')
        canConfirm = request.POST.get('usrConPass','')
        # cus = customer(C_Name=canName,C_Phone_num='077',C_Address='COlombo',C_email=canEmail,C_Password=canPass,C_rating=0)
        # if(canPhone == canConfirm):
        cus = service_providers()
        cus.SPName = canName
        cus.SPemail = canEmail
        cus.SPpassword = canPass
        cus.SPPhone_num = canPhone
        cus.SPAddress=canAddress
        cus.save()
        response_data = {}
        response_data['replyBot'] = "success"
        request.session['username'] = canEmail
        return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )

def verLogSP(request):
    if request.method == 'POST':
        canEmail = request.POST.get('usrEmail','')
        canPass = request.POST.get('usrPass','')
        request.session['spemail'] = canEmail
        print(canPass)
        candi = service_providers.objects.get(SPemail=canEmail);
        if (candi):
            if (candi.SPpassword == canPass):
                print("password is correct")
                response_data = {}
                response_data['replyBot'] = "success"
                # request.session['username'] = canEmail
                return HttpResponse(
                    json.dumps(response_data),
                    content_type="application/json"
                )