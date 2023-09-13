from django.shortcuts import render
from .models import MenuItem, Booking
from .serializers import MenuItemSerializer, BookingSerializer
from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from .forms import BookingForm
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.core import serializers
import json
from datetime import datetime


# # Create your views here.
# def index(request):
#     return render(request, 'index.html', {})

# class MenuItemsView(generics.ListCreateAPIView):
#     queryset = MenuItem.objects.all()
#     serializer_class = MenuItemSerializer

# class SingleMenuItemView(RetrieveUpdateAPIView, DestroyAPIView):
#     queryset = MenuItem.objects.all()
#     serializer_class = MenuItemSerializer


# class BookingViewSet(ModelViewSet):
#     # Secure this view, set the permission_classes property to a list containing IsAuthenticated.
#     permission_classes = [IsAuthenticated]
#     queryset = Booking.objects.all()
#     serializer_class = BookingSerializer

# @api_view()
# @permission_classes([IsAuthenticated])
# # @authentication_classes([TokenAuthentication])
# def msg(request):
#     return Response({"message":"This view is protected"})

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

def menu(request):
    menu_items = MenuItem.objects.all()
    return render(request, 'menu.html', {"menu": menu_items})

# Menu API
class MenuItemsView(generics.ListCreateAPIView):
    permission_classes = [AllowAny]
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.RetrieveDestroyAPIView):
    # The queryset attribute is not filtered, but the
    # DRF automatically filters it based on the pk
    # passed in the URL.
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

# Booking API
class BookingViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

def book(request):
    form = BookingForm
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form': form}
    return render(request, 'book.html', context)

def about(request):
    return render(request, "about.html")

@csrf_exempt
def bookings(request):
    if request.method == 'POST':
        data = json.load(request)
        exist = Booking.objects.filter(booking_date=data['booking_date']).filter(
            no_of_guests=data['no_of_guests']).exists()
        if exist==False:
            booking = Booking(
                name=data['name'],
                booking_date=data['booking_date'],
                no_of_guests=data['no_of_guests'],
            )
            booking.save()
        else:
            return HttpResponse("{'error':1}", content_type='application/json')

    date = request.GET.get('date',datetime.today().date())

    bookings = Booking.objects.all().filter(booking_date=date)
    booking_json = serializers.serialize('json', bookings)

    return HttpResponse(booking_json, content_type='application/json')


def reservations(request):
    date = request.GET.get('date', datetime.today().date())
    print("date: ", date)
    bookings = Booking.objects.all().filter(booking_date = date)
    booking_json = serializers.serialize('json', bookings)
    return render(request, 'bookings.html', {'bookings': booking_json})