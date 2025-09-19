# ALX Travel App - Database Modeling and Data Seeding

This project demonstrates database modeling, serializers, and data seeding in Django for a travel booking platform.

## Project Overview

The ALX Travel App is a Django-based travel booking platform that allows users to:
- Browse travel listings (properties available for booking)
- Make bookings for specific dates
- Leave reviews and ratings
- Manage their travel reservations

## Features

### Models
- **Listing**: Travel properties with details like location, price, amenities
- **Booking**: Reservation system with check-in/out dates and guest management
- **Review**: Rating and review system linked to bookings

### Serializers
- **ListingSerializer**: Handles listing data serialization with host information
- **BookingSerializer**: Manages booking data with validation and calculations
- **ReviewSerializer**: Processes review and rating data

### Data Seeding
- Management command to populate database with sample data
- Configurable number of listings and users
- Realistic sample data for testing and development

## Project Structure

```
alx_travel_app_0x00/
├── alx_travel_app/          # Django project settings
├── listings/                # Main app
│   ├── models.py           # Database models
│   ├── serializers.py      # API serializers
│   ├── views.py            # API views
│   ├── urls.py             # URL routing
│   └── management/
│       └── commands/
│           └── seed.py     # Database seeding command
├── manage.py               # Django management script
├── settings.py             # Project settings
├── urls.py                 # Main URL configuration
└── requirements.txt        # Dependencies
```

## Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd alx_travel_app_0x00
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run migrations**
   ```bash
   python manage.py migrate
   ```

4. **Seed the database**
   ```bash
   python manage.py seed
   ```

## Usage

### Database Seeding

The project includes a comprehensive seeding command:

```bash
# Basic seeding (10 listings, 5 additional users)
python manage.py seed

# Clear existing data and seed with custom amounts
python manage.py seed --clear --listings 20 --users 10

# Get help
python manage.py seed --help
```

### API Endpoints

- `GET /api/listings/` - List all travel listings
- `POST /api/listings/` - Create a new listing
- `GET /api/listings/{id}/` - Get specific listing details
- `PUT/PATCH /api/listings/{id}/` - Update listing
- `DELETE /api/listings/{id}/` - Delete listing

### Sample Data

The seeder creates realistic sample data including:
- **Users**: Hosts and guests with different roles
- **Listings**: Properties in various locations with amenities
- **Bookings**: Reservations with different statuses
- **Reviews**: Ratings and comments from completed stays

## Models

### Listing Model
- Title, description, location
- Price per night, guest capacity
- Bedrooms, bathrooms, amenities
- Host relationship and timestamps

### Booking Model
- Check-in/out dates with validation
- Guest count and total price calculation
- Status tracking (pending, confirmed, cancelled, completed)
- Special requests and metadata

### Review Model
- 1-5 star rating system
- Title and detailed comments
- Verification status
- Linked to specific bookings

## Serializers

### ListingSerializer
- Includes host username for easy identification
- Read-only fields for metadata
- Automatic host assignment on creation

### BookingSerializer
- Calculates total nights automatically
- Validates dates and guest counts
- Includes listing and guest information

### ReviewSerializer
- Rating validation (1-5 stars)
- Links to specific bookings
- Guest and listing information

## Database Seeding

The seeding command creates:
- **Hosts**: 3 default hosts for listings
- **Guests**: Configurable number of additional users
- **Listings**: Properties with realistic data
- **Bookings**: Reservations with various statuses
- **Reviews**: Ratings for completed bookings

## Development

### Running the Server
```bash
python manage.py runserver
```

### Admin Interface
```bash
python manage.py createsuperuser
# Then visit http://localhost:8000/admin/
```

### API Documentation
Visit `http://localhost:8000/swagger/` for interactive API documentation.

## Key Learning Outcomes

This project demonstrates:
- **Django Models**: Relational data modeling with proper relationships
- **Serializers**: Data transformation for API responses
- **Management Commands**: Custom Django commands for database operations
- **Data Seeding**: Automated database population for development
- **Validation**: Model and serializer-level data validation
- **Relationships**: Foreign keys, one-to-one, and many-to-many relationships

## Dependencies

- Django 5.2.6
- Django REST Framework 3.16.1
- Django CORS Headers 4.7.0
- DRF YASG 1.21.10 (API documentation)
- Django Environ 0.12.0 (Environment variables)

## License

This project is part of the ALX Software Engineering program.