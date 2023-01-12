from django.shortcuts import render
from .models import Menu
from django.core import serializers
from .models import Booking
from datetime import datetime, timedelta
import json
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse


def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def reservations(request):
    date = request.GET.get('date',datetime.today().date())
    bookings = Booking.objects.all().order_by('booking_date') #, 'reservation_slot')
    booking_json = serializers.serialize('json', bookings)
    return render(request, 'bookings.html',{"bookings":booking_json})

def book(request):
    return render(request, 'book.html')
    form = BookingForm()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request, 'book.html', context)



# Add your code here to create new views
def menu(request):
    menu_data = Menu.objects.all()
    main_data = {"menu": menu_data}
    return render(request, 'menu.html', {"menu": main_data})


def display_menu_item(request, pk=None): 
    if pk: 
        menu_item = Menu.objects.get(pk=pk) 
    else: 
        menu_item = "" 
    return render(request, 'menu_item.html', {"menu_item": menu_item}) 

@csrf_exempt
def bookings(request):
    if request.method == 'POST':
        data = json.load(request)

        booking = Booking(
            name=data['name'],
            booking_date=data['booking_date'],
            no_of_guests=data['no_of_guests'],
        )
        booking.save()
    
    date = request.GET.get('date',datetime.today().date())
    if date=='':
        date = datetime.today().date()
    #date_from = datetime.strptime(date, "%y-%m-%d %H:%M").date()
    #raise Exception(type(date), date)
    if(type(date) == type("string")):
        date_from = datetime.strptime(date, "%Y-%m-%d").date()
    else:
        date_from = date
    
    date_to = date_from + timedelta(days=1)
    #raise Exception(date_to, date_from)

    bookings = Booking.objects.all().filter(booking_date__gte=date_from,
                                booking_date__lt=date_to).order_by('booking_date')
    #raise Exception(bookings)

    booking_json = serializers.serialize('json', bookings)

    return HttpResponse(booking_json, content_type='application/json')