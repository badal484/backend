from rest_framework import serializers
from rest_framework_mongoengine.serializers import DocumentSerializer
from .models import UserDocument, Hotel, Booking, PropertyListing

# ------------------- Users -------------------
class UserSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=50)
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True, style={'input_type': 'password'})

    def create(self, validated_data):
        user = UserDocument(**validated_data)
        user.save()
        return user

# ------------------- Hotels -------------------
class HotelSerializer(DocumentSerializer):
    class Meta:
        model = Hotel
        fields = "__all__"

# ------------------- Bookings -------------------
class BookingSerializer(DocumentSerializer):
    class Meta:
        model = Booking
        fields = ['hotelId', 'name', 'email', 'phone', 'checkIn', 'checkOut', 'guests']

# ------------------- Property Listing -------------------
class PropertyListingSerializer(DocumentSerializer):
    class Meta:
        model = PropertyListing
        fields = [
            "name", "phone", "email", "propertyType", "city",
            "message", "facilities", "created_at"
        ]
