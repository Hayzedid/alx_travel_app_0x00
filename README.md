# ALX Travel App

A Django-based travel listing platform built with Django REST Framework, featuring MySQL database integration, Swagger API documentation, and CORS support.

## 🚀 Features

- **Django REST Framework**: Modern API development with powerful features
- **MySQL Database**: Robust database integration with environment-based configuration
- **Swagger Documentation**: Automatic API documentation at `/swagger/`
- **CORS Support**: Cross-Origin Resource Sharing for frontend integration
- **Celery Integration**: Background task processing capabilities
- **Environment Configuration**: Secure configuration management with django-environ

## 📋 Requirements

- Python 3.8+
- MySQL Server
- RabbitMQ (for Celery, optional)

## 🛠️ Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Hayzedid/alx_travel_app.git
   cd alx_travel_app
   ```

2. **Create virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables:**
   Copy `.env.example` to `.env` and configure your settings:
   ```bash
   cp .env.example .env
   ```

   Update the `.env` file with your database credentials and other settings.

5. **Set up MySQL database:**
   Create a MySQL database named `alx_travel_app_db` or update the `DB_NAME` in your `.env` file.

6. **Run migrations:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

7. **Create superuser (optional):**
   ```bash
   python manage.py createsuperuser
   ```

## 🚀 Running the Application

1. **Start the development server:**
   ```bash
   python manage.py runserver
   ```

2. **Access the application:**
   - API Base URL: `http://localhost:8000/api/`
   - Admin Panel: `http://localhost:8000/admin/`
   - Swagger Documentation: `http://localhost:8000/swagger/`
   - ReDoc Documentation: `http://localhost:8000/redoc/`

## 📚 API Endpoints

### Listings
- `GET /api/listings/` - List all listings
- `POST /api/listings/` - Create a new listing
- `GET /api/listings/{id}/` - Get listing details
- `PUT /api/listings/{id}/` - Update a listing
- `DELETE /api/listings/{id}/` - Delete a listing

### API Overview
- `GET /api/overview/` - Get API endpoints overview

## 🏗️ Project Structure

```
alx_travel_app/
├── alx_travel_app/          # Main Django project
│   ├── __init__.py
│   ├── settings.py         # Django settings with environment config
│   ├── urls.py            # Main URL configuration
│   ├── wsgi.py
│   └── asgi.py
├── listings/               # Listings app
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py          # Listing model
│   ├── serializers.py     # DRF serializers
│   ├── tests.py
│   ├── urls.py            # App URL configuration
│   └── views.py           # API views
├── venv/                  # Virtual environment (not in repo)
├── .env                   # Environment variables (not in repo)
├── .env.example          # Environment template
├── requirements.txt      # Python dependencies
├── README.md             # This file
└── manage.py             # Django management script
```

## 🔧 Configuration

### Environment Variables

The application uses environment variables for configuration. Key variables include:

- `SECRET_KEY`: Django secret key
- `DEBUG`: Debug mode (True/False)
- `ALLOWED_HOSTS`: Comma-separated list of allowed hosts
- `DB_ENGINE`: Database engine
- `DB_NAME`: Database name
- `DB_USER`: Database user
- `DB_PASSWORD`: Database password
- `DB_HOST`: Database host
- `DB_PORT`: Database port
- `CELERY_BROKER_URL`: Celery broker URL
- `CELERY_RESULT_BACKEND`: Celery result backend

### Database Setup

1. Install MySQL Server
2. Create a database: `CREATE DATABASE alx_travel_app_db;`
3. Update `.env` with your MySQL credentials
4. Run migrations: `python manage.py migrate`

## 🧪 Testing

Run tests with:
```bash
python manage.py test
```

## 📖 Documentation

- **Swagger UI**: `http://localhost:8000/swagger/`
- **ReDoc**: `http://localhost:8000/redoc/`

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

This project is licensed under the BSD License - see the LICENSE file for details.

## 👥 Authors

- ALX Student - Initial work

## 🙏 Acknowledgments

- Django Project
- Django REST Framework
- ALX Africa for the learning opportunity
