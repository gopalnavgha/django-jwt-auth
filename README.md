# Django JWT Authentication API

🔐 A simple Django REST Framework project implementing JWT-based authentication.

## 🚀 Features

- User Registration API (`/api/register/`)
- JWT Login API (`/api/login/`)
- Protected API View (`/api/protected/`)
- Bootstrap-based Frontend to test APIs
- Token stored in memory (can be extended with refresh)

---

## 📁 Project Structure

authproject/
├── accounts/
│ ├── views.py
│ ├── urls.py
│ └── ...
├── authproject/
│ ├── settings.py
│ └── urls.py
├── templates/
│ └── home.html
├── manage.py
├── .gitignore


---

## ⚙️ Setup Instructions

1. Clone the repo:

>git clone https://github.com/yourusername/django-jwt-auth.git
>cd django-jwt-auth

Create virtual environment:


>python -m venv venv
>source venv/bin/activate  # Windows: venv\Scripts\activate
Install requirements:


>pip install django djangorestframework djangorestframework-simplejwt python-decouple
Apply migrations:


>python manage.py migrate
Run server:


>python manage.py runserver
🧪 API Test (via Browser UI)
Visit http://localhost:8000/api/

Use the HTML interface to register, login, and call protected route.








