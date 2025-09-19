from rest_framework import serializers
from .models import Listing, Booking, Review
from django.contrib.auth.models import User


class ListingSerializer(serializers.ModelSerializer):
    """
    Serializer for the Listing model.
    Handles serialization and deserialization of Listing instances.
    """
    host_username = serializers.CharField(source='host.username', read_only=True)

    class Meta:
        model = Listing
        fields = [
            'id', 'title', 'description', 'location', 'price_per_night',
            'max_guests', 'bedrooms', 'bathrooms', 'amenities',
            'created_at', 'updated_at', 'is_active', 'host_username'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at', 'host_username']

    def create(self, validated_data):
        """
        Create a new listing instance.
        """
        validated_data['host'] = self.context['request'].user
        return super().create(validated_data)


class BookingSerializer(serializers.ModelSerializer):
    """
    Serializer for the Booking model.
    Handles serialization and deserialization of Booking instances.
    """
    guest_username = serializers.CharField(source='guest.username', read_only=True)
    listing_title = serializers.CharField(source='listing.title', read_only=True)
    listing_location = serializers.CharField(source='listing.location', read_only=True)
    total_nights = serializers.SerializerMethodField()
    
    class Meta:
        model = Booking
        fields = [
            'id', 'listing', 'guest', 'check_in_date', 'check_out_date',
            'number_of_guests', 'total_price', 'status', 'special_requests',
            'created_at', 'updated_at', 'guest_username', 'listing_title',
            'listing_location', 'total_nights'
        ]
        read_only_fields = [
            'id', 'created_at', 'updated_at', 'guest_username', 
            'listing_title', 'listing_location', 'total_nights'
        ]

    def get_total_nights(self, obj):
        """Calculate total number of nights"""
        return (obj.check_out_date - obj.check_in_date).days

    def create(self, validated_data):
        """
        Create a new booking instance.
        """
        validated_data['guest'] = self.context['request'].user
        return super().create(validated_data)

    def validate(self, data):
        """
        Validate booking data.
        """
        from django.core.exceptions import ValidationError
        from datetime import date
        
        check_in = data.get('check_in_date')
        check_out = data.get('check_out_date')
        number_of_guests = data.get('number_of_guests')
        listing = data.get('listing')
        
        # Validate dates
        if check_in and check_out:
            if check_out <= check_in:
                raise serializers.ValidationError("Check-out date must be after check-in date.")
            
            if check_in < date.today():
                raise serializers.ValidationError("Check-in date cannot be in the past.")
        
        # Validate number of guests
        if listing and number_of_guests:
            if number_of_guests > listing.max_guests:
                raise serializers.ValidationError(
                    f"Number of guests ({number_of_guests}) exceeds maximum allowed ({listing.max_guests})."
                )
        
        return data


class ReviewSerializer(serializers.ModelSerializer):
    """
    Serializer for the Review model.
    Handles serialization and deserialization of Review instances.
    """
    guest_username = serializers.CharField(source='guest.username', read_only=True)
    listing_title = serializers.CharField(source='listing.title', read_only=True)
    
    class Meta:
        model = Review
        fields = [
            'id', 'listing', 'guest', 'booking', 'rating', 'title', 'comment',
            'created_at', 'updated_at', 'is_verified', 'guest_username',
            'listing_title'
        ]
        read_only_fields = [
            'id', 'created_at', 'updated_at', 'is_verified',
            'guest_username', 'listing_title'
        ]

    def create(self, validated_data):
        """
        Create a new review instance.
        """
        validated_data['guest'] = self.context['request'].user
        return super().create(validated_data)

    def validate_rating(self, value):
        """
        Validate rating value.
        """
        if value < 1 or value > 5:
            raise serializers.ValidationError("Rating must be between 1 and 5.")
        return value
