

# 🧠 Django Telegram Bot Integration with Celery

This project demonstrates how to integrate a **Telegram Bot** with a **Django REST API**, using **Celery** and **Redis** to send Telegram messages as background tasks.

---

## 📌 Features

- Telegram Bot collects usernames via `/start` command and stores them in Django.
- Django Admin displays registered Telegram users.
- On user registration (via web/API), Django sends a **welcome message** to their Telegram.
- Celery + Redis handles message sending asynchronously.

---

## 🏗️ Tech Stack

- Django 5.2+
- Django REST Framework
- Telegram Bot API (via `python-telegram-bot`)
- Celery (Background task queue)
- Redis (Message broker for Celery)
- PostgreSQL/SQLite (default DB)
- python-decouple (for environment variables)

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/your-repo.git
cd your-repo
 
### 2. Create & Activate Virtual Environment

