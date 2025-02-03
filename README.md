# Bookstore API

This is a simple Django-based Bookstore API that allows users to manage books in an online bookstore. 
The project is containerized using Docker for easier deployment and setup.

## Prerequisites

Ensure you have the following installed on your machine:

- Docker: https://www.docker.com/get-started
- Docker Compose: https://docs.docker.com/compose/install/

## Project Setup

### 1. Clone the Repository
Clone the repository to your local machine:

```bash
git clone https://github.com/deshmukh-rushi/drf-book-store-backennd-api.git
cd drf-book-store-backennd-api

Activate the virtual environment



2. Configuration
Before running the application, make sure you have set up your environment variables correctly in the Django settings. In particular, configure the database settings in settings.py to connect to PostgreSQL.

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'bookstore',
        'USER': 'postgres',
        'PASSWORD': 'gurudevDatta',
        'HOST': 'db',
        'PORT': '5432',
    }
}

3. Build and Start the Containers
Run the following command to build and start your Docker containers:
docker-compose up --build

This command will:
    Build the web service from the Dockerfile.
    Start the db service (PostgreSQL database).
    Start the Django application on http://localhost:8000

4. Run Migrations
Once the containers are running, execute the following command to apply migrations:

docker-compose exec web python manage.py migrate

5. Access the API
Once everything is set up, you can access the API at:

http://localhost:8000/api/
You can use Postman or any HTTP client to interact with the API.

6. Stopping the Containers
To stop the containers, use:


docker-compose down
This will stop and remove the containers, but the database and web container data will persist. You can always restart with docker-compose up.


Notes
Database: PostgreSQL is used as the backend database.
Django Version: Make sure you're using the correct version of Django and the required dependencies in requirements.txt.
Docker: Docker Compose orchestrates the services (web for Django and db for PostgreSQL).
