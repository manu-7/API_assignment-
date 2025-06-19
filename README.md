
# Django REST API with Celery & Telegram Bot Integration

This project demonstrates a production-ready Django backend using Django REST Framework (DRF) with Token Authentication, Celery for background tasks, Redis as a broker, and Telegram Bot integration to interact with users.






## Features

User Registration & Login (via API and Web)

 Public API Endpoint (accessible by anyone)

 Protected API Endpoint (Token-based access)

 Send Welcome Email via Celery after registration

 Telegram Bot Integration to collect usernames via /start command

 Store Telegram data in database

 Proper Production Configuration using .env
 


## Tech Stack

Python 3.12+

Django 5.2+

Django REST Framework

Celery

Redis

python-telegram-bot (v13.15)

PostgreSQL / SQLite

Python Decouple

Git & GitHub


##  Setup Instructions

###  1.Create & Activate Virtual Environment

     python -m venv venv
     # Windows
     venv\Scripts\activate

### 2. Install Dependencies
    pip install -r requirements.txt

### 3. Setup Environment Variables

    SECRET_KEY=your-django-secret-key
    DEBUG=False
    ALLOWED_HOSTS=127.0.0.1,localhost
    DATABASE_URL=sqlite:///db.sqlite3  # or your PostgreSQL URL
    TELEGRAM_BOT_TOKEN=your_bot_token_here
    EMAIL_HOST=smtp.example.com
    EMAIL_PORT=587
    EMAIL_HOST_USER=your_email@example.com
    EMAIL_HOST_PASSWORD=your_password
    EMAIL_USE_TLS=True
### 4. Apply Migrations

    python manage.py makemigrations
    python manage.py migrate

### 5. Create Superuser (for Admin UI)

    python manage.py createsuperuser

### 6. Run Development Server

    python manage.py runserver

##  Running Celery + Redis
### Start Redis Server (use Docker for simplicity)

    docker run -d -p 6379:6379 redis

### Start Celery Worker (in a new terminal)

    celery -A myproject worker --loglevel=info --pool=solo  

### How Celery + Redis Works in This Project

    User registers → Django calls a Celery task → Task is sent to Redis → Celery Worker picks it → Task runs (e.g. send message/email)

### Celery Setup Summary

    myproject/
    │
    ├── myproject/              # Django settings, celery.py lives here
    │   ├── __init__.py         # Initializes celery app
    │   └── celery.py           # Celery configuration
    │
    ├── core/                   # Your Django app
    │   ├── tasks.py            # Background task lives here
    │
    ├── telegram_bot.py                  
    ├── requirements.txt
    ├── .env
    └── manage.py


## Telegram Bot Integration

### 1. Bot setup

Create a bot via @BotFather and get your BOT_TOKEN.

Add to .env:

    TELEGRAM_BOT_TOKEN=your_token_here



Now, open Telegram, search for your bot, and type /start.

The bot will collect your Telegram username and send it to the Django backend.


### 2. Model to Store Telegram Users

    # models.py

    class TelegramUser(models.Model):
    username = models.CharField(max_length=150, unique=True)
    chat_id = models.CharField(max_length=50, unique=True)
    first_name = models.CharField(max_length=150, blank=True)
    last_name = models.CharField(max_length=150, blank=True)


    python manage.py makemigrations
    python manage.py migrate

### 3. Bot Script (Telegram_bot.py)

### 4. How it Works
User sends /start to bot.

Bot collects user info and sends it to Django via API.

Django saves the info to TelegramUser table.

## API Documentation

        | Function      | URL             |    Method   |     Auth    |        Description                          |
    | ----------------- | --------------------- | ------ | ------- | --------------------------------------  |
    | Public API        | `/api/public/`        | GET    | ❌       | Open to everyone                       |
    | Protected API     | `/api/protected/`     | GET    | ✅ Token | Only for authenticated users           |
    | Obtain Token      | `/api/token-auth/`    | POST   | ❌       | Get token by sending username/password |
    | User Registration | `/api/register/`      | POST   | ❌       | Creates user & triggers Celery task    |
    | Telegram Save API | `/api/telegram/save/` | POST   | ❌ (Bot) | Receives and stores Telegram username  |


###  🔑 Get Auth Token
    POST /api/token-auth/
    
    {
    "username": "testuser",
    "password": "password123"
    }

### 🔐 Access Protected API

    GET /api/protected/
    Authorization: Token your_token_here

### 👤 Register User (Triggers Celery Task)

    POST /api/register/
    {
    "username": "MS2",
    "email": "MS2@example.com",
    "password": "12345678"
    }


# 📌 Notes

Make sure Redis is running before starting Celery.

Bot must be running to receive /start commands and send data to backend.

You can use Postman to test the APIs easily.

# ✍️ Author

Manu Singh – https://github.com/manu-7




