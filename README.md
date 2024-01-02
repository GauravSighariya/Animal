
# Animal CRUD APIs

This repository contains a set of APIs for managing animal data, including:

Creating new animal records
Retrieving existing animal information
Updating animal details
Deleting animal records

Key features:

CRUD functionality for comprehensive animal data management
Token-based authentication for secure API access
User permissions to control access to specific API actions (e.g., deletion restricted to superusers)
Management command for convenient data creation from the command line
Clear and concise README for easy setup and usage

Getting Started:

1. Clone the repository:
```
git clone https://github.com/GauravSighariya/Animal
```
2. Install dependencies:
```
pip install -r requirements.txt
```
3. Set up database configuration:
  Create a database and edit the settings.py file with your database credentials.

4. Run migrations:
```
python manage.py makemigrations
python manage.py migrate
```

5. Create superuser (optional):
```
python manage.py createsuperuser
```

# API Endpoints:
```
  CREATE: /api/animals/ (POST)
  RETRIEVE:/api/animals/ (GET)
  MODIFY: /api/animals/<animal_id>/ (PUT, PATCH)
  DELETE: /api/animals/<animal_id>/ (DELETE)
```
  Authentication:

Obtain a token using the /api/token/ endpoint.
  Include the token in the Authorization header of subsequent API requests (e.g., Authorization: Token <your_token>).

Permissions:

Superusers have full access to all API actions.
Normal users can create, retrieve, and modify animal data, but cannot delete.
Management Command:

Create sample users data using:
```
python manage.py create_fake_user
```

   
