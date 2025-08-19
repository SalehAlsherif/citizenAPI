
A scalable and secure backend service for managing citizen data, built with Django REST Framework. Designed for extensibility, cross-platform compatibility, and robust authentication.

## 🚀 Features

- 🔐 API key-based service-to-service authentication
- 📦 RESTful endpoints for CRUD operations on citizen records
- 🧪 Integrated testing with pytest
- 🛡️ Secure permission management and input validation
- 🖥️ Cross-platform support (Windows/MSYS2, Linux, macOS)

## 🧰 Tech Stack

- **Backend**: Django, Django REST Framework
- **Auth**: Custom API key middleware
- **Database**: PostgreSQL (default), SQLite (for dev)

🧪 Running Tests
bash
pytest


## 📦 Installation
- git clone https://github.com/your-username/citizens.git
- cd citizens
- python manage.py makemigrations citizens 
- python manage.py migrate        


## Creating a admin User:

-python manage.py createsuperuser 
## Runing:

-python manage.py runserver

-visit http://127.0.0.1:8000/admin/ to create API key

🔑 Authentication
All endpoints require a valid API key passed via the Authorization header:
 - Authorization: Api-Key <your_api_key_here>

  





