from django.contrib import admin
from .models import Listing


@admin.register(Listing)
class ListingAdmin(admin.ModelAdmin):
    """Admin configuration for Listing model."""
    list_display = ['title', 'location', 'price_per_night', 'max_guests', 'is_active', 'created_at']
    list_filter = ['is_active', 'created_at', 'location']
    search_fields = ['title', 'description', 'location']
    readonly_fields = ['created_at', 'updated_at']
    list_editable = ['is_active']
    ordering = ['-created_at']
