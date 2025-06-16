

# Django REST API with Celery, Email & Authentication

This is a small backend project built using Django and Django REST Framework to showcase core backend features like API development, token-based authentication, background task processing with Celery, and email notifications.

---

## Features Completed

###  Django Setup & Configuration
- Initialized a Django project with REST Framework.
- Project structured cleanly with separate `api` apps.
- Environment variables handled using `python-decouple` (`.env` used for secrets like SECRET_KEY, email credentials).
- Production-ready settings with `DEBUG=False` and allowed hosts set.
- Email backend configured to send emails using Gmail SMTP.

---

### Authentication
- Token-based authentication (DRF’s TokenAuth) is in place.
- Users can obtain a token by providing their credentials.

**POST Endpoint:**  
