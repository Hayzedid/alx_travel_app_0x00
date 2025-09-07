from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Listing
from .serializers import ListingSerializer


@api_view(['GET'])
def api_overview(request):
    """
    API Overview endpoint that provides information about available endpoints.
    """
    api_urls = {
        'List': '/api/listings/',
        'Detail View': '/api/listings/<str:pk>/',
        'Create': '/api/listings/',
        'Update': '/api/listings/<str:pk>/',
        'Delete': '/api/listings/<str:pk>/',
        'Swagger Documentation': '/swagger/',
        'ReDoc Documentation': '/redoc/',
    }
    return Response(api_urls)


class ListingViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing travel listings.
    Provides CRUD operations for listings.
    """
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer
