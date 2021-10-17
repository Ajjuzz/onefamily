from django.shortcuts import render

# Create your views here.

from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib.auth.models import Group, User, auth
from .models import Register, Country, State, District, Contact
from django.contrib import messages
from django.http import JsonResponse
from django.core.paginator import Paginator

def home(request):
    country_qs = Country.objects.all()
    state_qs = State.objects.all()
    district_qs = District.objects.all()

    if request.method == 'POST':
        Name = request.POST['contactName']
        Email = request.POST['contactEmail']
        Message = request.POST['contactMessage']

        contact = Contact(Name=Name,Email=Email,Message=Message)
        contact.save()
        messages.success(request,'Your Message will be Shortly reviewed !')
        return redirect('/')

    return render(request, 'app/index.html', {'country_qs': country_qs, 'state_qs': state_qs, 'district_qs': district_qs})


def register(request):
    country_qs = Country.objects.all()
    state_qs = State.objects.all()
    district_qs = District.objects.all()

    if request.method == 'POST':
        name = request.POST['name']
        phoneNo = request.POST['phoneNo']
        country = request.POST['country'] 
        state= request.POST['state']
        district = request.POST['district']
        city = request.POST['city']
        blood = request.POST['blood']
        age = request.POST['age']
        gender = request.POST['gender']


        
        objects = Register(name=name, phoneNo=phoneNo, country=country, city=city, state_id=state,
                          district_id=district,  blood=blood, age=age, gender=gender)

        objects.save()
        messages.success(request,'Your are Successfully Registered !')
        return redirect('/')
    return render(request, 'app/register.html', {'country_qs': country_qs, 'state_qs': state_qs, 'district_qs': district_qs})


def donar(request):

    blood_search = request.POST.get('blood_search')
    state_search = request.POST.get('state_search')
    district_search =  request.POST.get('district_search')
            
    donar_page = Register.objects.filter( blood=blood_search, district=district_search, state=state_search).all()
    if donar_page:
        return render(request, 'app/donar.html', {'donar_page': donar_page})
    else:
        messages.success(request,'Sorry, Currently No donars available for your search results. We will take this request and back to you soon!')
    return render(request, 'app/donar.html')


def loader(requst):
    return render(requst,'app/loader.html')




    
