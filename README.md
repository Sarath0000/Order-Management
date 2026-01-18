Order Management System (Django + DRF)

This project is a backend REST API built using Django Rest Framework (DRF) with JWT authentication.
It supports role-based access with Admin and Customer users


Python
Django
Django REST Framework
JWT Authentication (SimpleJWT)
SQLite (default)


Setup Instructions

    1️ Clone the project
        git clone https://github.com/Sarath0000/Order-Management.git

    2️ Create virtual environment
        python -m venv venv
        Activate it : venv\Scripts\activate

    3️ Install dependencies
        pip install -r requirements.txt

    4️ Apply migrations
        python manage.py makemigrations
        python manage.py migrate

    5️ Run the server
        python manage.py runserver
        Server will start at : Copy code http://127.0.0.1:8000/


Authentication Flow (JWT)

User registers using API

User logs in using API

Server returns JWT access token

Token is sent in Authorization header for protected APIs

API Usage Guide (Postman)
    Authorization Header (for protected APIs)  Authorization: Bearer <ACCESS_TOKEN>

API List

Register User
    Method: POST
    Endpoint : /api/accounts/register/
    Sample Request
        {
            "username": "user1",
            "password": "1234"
        }
    Sample Response
        {
            "message": "Customer registered successfully"
        }

Login (JWT)
    Method: POST
    Endpoint : /api/login/
    Sample Request
        {
            "username": "user1",
            "password": "1234"
        }
    Sample Response
        {
            "refresh": "eyJhbGciOiJIUzI1NiIs...",
            "access": "eyJhbGciOiJIUzI1NiIs..."
        }
Create Product (Admin Only)
    Method: POST
    Endpoint : /api/products/create/
    Authorization: Bearer <ACCESS_TOKEN>
    Sample Request
        {
            "name": "Bat",
            "price": 1200,
            "quantity": 10
        }
        Sample Response
        {
            "id": 1,
            "name": "Bat",
            "price": "1200.00",
            "quantity": 10
        }
List Products (Admin & Customer)
    Method: GET
    Endpoint : /api/products/
    Authorization: Bearer <ACCESS_TOKEN>
    Sample Response
    [
        {
            "id": 1,
            "name": "Bat",
            "price": "1200.00",
            "quantity": 10
        }
    ]
Update Product (Admin Only)
    Method: PUT
    Endpoint : /api/products/<id>/
    Authorization: Bearer <ACCESS_TOKEN>
    Sample Request
        {
            "quantity": 15
        }
    Sample Response
        {
            "id": 1,
            "name": "Bat",
            "price": "1200.00",
            "quantity": 15
        }
Delete Product (Admin Only)
    Method: DELETE
    Endpoint : /api/products/<id>/delete/
    Authorization: Bearer <ACCESS_TOKEN>
    Sample Response
        {
            "message": "Product deleted"
        }

Roles & Permissions

Role-Admin

Permissions-Create, update, delete, view products

Role-Customer

Permissions-view products





