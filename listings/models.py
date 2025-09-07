from django.db import models
from django.contrib.auth.models import User


class Listing(models.Model):
    """
    Model for travel listings in the ALX Travel App.
    """
    title = models.CharField(max_length=200, help_text="Title of the travel listing")
    description = models.TextField(help_text="Detailed description of the listing")
    location = models.CharField(max_length=100, help_text="Location of the property")
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2, help_text="Price per night in USD")
    max_guests = models.PositiveIntegerField(default=1, help_text="Maximum number of guests")
    bedrooms = models.PositiveIntegerField(default=1, help_text="Number of bedrooms")
    bathrooms = models.PositiveIntegerField(default=1, help_text="Number of bathrooms")
    amenities = models.JSONField(default=list, help_text="List of amenities available")

    # Metadata
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    # Foreign keys
    host = models.ForeignKey(User, on_delete=models.CASCADE, related_name='listings')

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Travel Listing"
        verbose_name_plural = "Travel Listings"

    def __str__(self):
        return f"{self.title} - {self.location}"
