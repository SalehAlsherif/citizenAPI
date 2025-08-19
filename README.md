
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



## Runing:

-python manage.py runserver
-works with all default CRUD operations
-For Examble List GET:
-http://127.0.0.1:8000/citizens/ 

You now have these endpoints:

Method	Endpoint	Action

GET	/citizens/	Read all

POST	/citizens/	Create new

GET	/citizens/<id>/	Read one

PUT	/citizens/<id>/	Update

DELETE	/citizens/<id>/	Delete

Use tools like Postman, curl, or Django’s Browsable API to test

## Creating a admin User:

-python manage.py createsuperuser 

-visit http://127.0.0.1:8000/admin/ to create API key


🔑 Authentication
All endpoints require a valid API key passed via the Authorization header:
 - Authorization: Api-Key <your_api_key_here>

  





