"""
Management command to seed the database with sample data for the ALX Travel App.
This command creates sample listings, users, bookings, and reviews for testing and development.
"""
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import date, timedelta
from decimal import Decimal
import random
from alx_travel_app.listings.models import Listing, Booking, Review


class Command(BaseCommand):
    help = 'Seed the database with sample travel listings, bookings, and reviews'

    def add_arguments(self, parser):
        parser.add_argument(
            '--clear',
            action='store_true',
            help='Clear existing data before seeding',
        )
        parser.add_argument(
            '--listings',
            type=int,
            default=10,
            help='Number of listings to create (default: 10)',
        )
        parser.add_argument(
            '--users',
            type=int,
            default=5,
            help='Number of additional users to create (default: 5)',
        )

    def handle(self, *args, **options):
        self.stdout.write(
            self.style.SUCCESS('Starting database seeding...')
        )

        # Clear existing data if requested
        if options['clear']:
            self.clear_data()

        # Create users
        users = self.create_users(options['users'])
        
        # Create listings
        listings = self.create_listings(options['listings'], users)
        
        # Create bookings
        bookings = self.create_bookings(listings, users)
        
        # Create reviews
        self.create_reviews(bookings)

        self.stdout.write(
            self.style.SUCCESS(
                f'Successfully seeded database with:\n'
                f'- {len(users)} users\n'
                f'- {len(listings)} listings\n'
                f'- {len(bookings)} bookings\n'
                f'- {len(Review.objects.all())} reviews'
            )
        )

    def clear_data(self):
        """Clear existing data from the database"""
        self.stdout.write('Clearing existing data...')
        
        Review.objects.all().delete()
        Booking.objects.all().delete()
        Listing.objects.all().delete()
        
        # Don't delete superuser
        User.objects.filter(is_superuser=False).delete()
        
        self.stdout.write(self.style.WARNING('Existing data cleared.'))

    def create_users(self, num_users):
        """Create sample users"""
        self.stdout.write('Creating users...')
        
        users = []
        
        # Create hosts
        host_data = [
            {'username': 'john_host', 'email': 'john@example.com', 'first_name': 'John', 'last_name': 'Smith'},
            {'username': 'sarah_host', 'email': 'sarah@example.com', 'first_name': 'Sarah', 'last_name': 'Johnson'},
            {'username': 'mike_host', 'email': 'mike@example.com', 'first_name': 'Mike', 'last_name': 'Wilson'},
        ]
        
        for data in host_data:
            user, created = User.objects.get_or_create(
                username=data['username'],
                defaults={
                    'email': data['email'],
                    'first_name': data['first_name'],
                    'last_name': data['last_name'],
                }
            )
            if created:
                user.set_password('password123')
                user.save()
            users.append(user)
        
        # Create additional users
        for i in range(num_users):
            username = f'user_{i+1}'
            email = f'user{i+1}@example.com'
            
            user, created = User.objects.get_or_create(
                username=username,
                defaults={
                    'email': email,
                    'first_name': f'User{i+1}',
                    'last_name': 'LastName',
                }
            )
            if created:
                user.set_password('password123')
                user.save()
            users.append(user)
        
        return users

    def create_listings(self, num_listings, users):
        """Create sample listings"""
        self.stdout.write('Creating listings...')
        
        locations = [
            'New York, NY', 'Los Angeles, CA', 'Chicago, IL', 'Houston, TX',
            'Phoenix, AZ', 'Philadelphia, PA', 'San Antonio, TX', 'San Diego, CA',
            'Dallas, TX', 'San Jose, CA', 'Austin, TX', 'Jacksonville, FL',
            'Fort Worth, TX', 'Columbus, OH', 'Charlotte, NC', 'San Francisco, CA',
            'Indianapolis, IN', 'Seattle, WA', 'Denver, CO', 'Washington, DC'
        ]
        
        property_types = [
            'Apartment', 'House', 'Condo', 'Villa', 'Cottage', 'Studio',
            'Loft', 'Townhouse', 'Penthouse', 'Cabin'
        ]
        
        amenities_lists = [
            ['WiFi', 'Kitchen', 'Parking', 'Pool'],
            ['WiFi', 'Kitchen', 'Gym', 'Balcony'],
            ['WiFi', 'Kitchen', 'Hot Tub', 'Garden'],
            ['WiFi', 'Kitchen', 'Pool', 'Gym', 'Balcony'],
            ['WiFi', 'Kitchen', 'Parking', 'Garden', 'Hot Tub'],
            ['WiFi', 'Kitchen', 'Pool', 'Gym', 'Balcony', 'Garden'],
        ]
        
        listings = []
        
        for i in range(num_listings):
            listing = Listing.objects.create(
                title=f"{random.choice(property_types)} in {random.choice(locations)}",
                description=self.generate_description(),
                location=random.choice(locations),
                price_per_night=Decimal(random.uniform(50, 500)).quantize(Decimal('0.01')),
                max_guests=random.randint(1, 8),
                bedrooms=random.randint(1, 5),
                bathrooms=random.randint(1, 4),
                amenities=random.choice(amenities_lists),
                host=random.choice(users[:3]),  # Use first 3 users as hosts
                is_active=random.choice([True, True, True, False])  # 75% active
            )
            listings.append(listing)
        
        return listings

    def create_bookings(self, listings, users):
        """Create sample bookings"""
        self.stdout.write('Creating bookings...')
        
        bookings = []
        active_listings = [l for l in listings if l.is_active]
        
        for _ in range(min(15, len(active_listings) * 2)):  # Create up to 15 bookings
            listing = random.choice(active_listings)
            guest = random.choice(users[3:])  # Use users after the first 3 as guests
            
            # Generate random dates
            start_date = date.today() + timedelta(days=random.randint(1, 30))
            end_date = start_date + timedelta(days=random.randint(1, 7))
            
            # Calculate total price
            nights = (end_date - start_date).days
            total_price = listing.price_per_night * nights
            
            booking = Booking.objects.create(
                listing=listing,
                guest=guest,
                check_in_date=start_date,
                check_out_date=end_date,
                number_of_guests=random.randint(1, min(4, listing.max_guests)),
                total_price=total_price,
                status=random.choice(['pending', 'confirmed', 'completed']),
                special_requests=random.choice([
                    None, None, None,  # 75% no special requests
                    "Late check-in requested",
                    "Please provide extra towels",
                    "Vegetarian breakfast preferred",
                    "Quiet room preferred"
                ])
            )
            bookings.append(booking)
        
        return bookings

    def create_reviews(self, bookings):
        """Create sample reviews"""
        self.stdout.write('Creating reviews...')
        
        # Only create reviews for completed bookings
        completed_bookings = [b for b in bookings if b.status == 'completed']
        
        review_titles = [
            "Amazing stay!", "Great location", "Perfect for families",
            "Beautiful property", "Highly recommended", "Excellent host",
            "Clean and comfortable", "Great value", "Will stay again",
            "Outstanding experience", "Lovely place", "Fantastic location"
        ]
        
        review_comments = [
            "The property was exactly as described. Clean, comfortable, and in a great location.",
            "Host was very responsive and helpful. The place had everything we needed.",
            "Beautiful property with amazing amenities. Would definitely stay again.",
            "Great location, easy access to attractions. The place was spotless.",
            "Perfect for our family vacation. Kids loved the pool and garden.",
            "Excellent value for money. The host was very accommodating.",
            "Stunning views and modern amenities. Highly recommend this place.",
            "Clean, comfortable, and well-equipped. Great communication with host.",
            "Fantastic stay! The property exceeded our expectations.",
            "Wonderful experience. The host was friendly and the place was perfect.",
            "Great location and beautiful property. Will definitely book again.",
            "Amazing amenities and excellent service. Highly recommended!"
        ]
        
        for booking in completed_bookings[:8]:  # Create reviews for up to 8 completed bookings
            Review.objects.create(
                listing=booking.listing,
                guest=booking.guest,
                booking=booking,
                rating=random.randint(3, 5),  # Mostly positive reviews
                title=random.choice(review_titles),
                comment=random.choice(review_comments),
                is_verified=True
            )

    def generate_description(self):
        """Generate a random property description"""
        descriptions = [
            "Beautiful and spacious property in a prime location. Perfect for both business and leisure travelers.",
            "Modern and well-appointed accommodation with all the amenities you need for a comfortable stay.",
            "Charming property with character and modern conveniences. Ideal for families and groups.",
            "Luxurious accommodation with stunning views and top-notch amenities.",
            "Cozy and comfortable space in a great neighborhood. Close to all major attractions.",
            "Elegant property with contemporary design and excellent facilities.",
            "Spacious and bright accommodation with everything you need for a perfect stay.",
            "Stylish property in a convenient location with easy access to transportation.",
            "Well-maintained accommodation with modern amenities and friendly neighborhood.",
            "Charming and comfortable space perfect for a relaxing getaway."
        ]
        return random.choice(descriptions)
