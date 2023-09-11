from rest_framework import serializers
from .models import Booking, MenuItem


class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        # Fetch the objects from the menu item model:
        model = MenuItem
        fields = ['title', 'price', 'inventory']


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        # Fetch all the objects from the booking model:
        model = Booking
        fields = '__all__'