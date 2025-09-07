from rest_framework import serializers
from .models import Listing


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
