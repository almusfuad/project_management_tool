# Project Management Tool 
 
This is a simple API for managing projects, tasks, and teams. It allows users to create, update, delete, and view projects and tasks. 
 
## Setup Instructions 

Follow these steps to set up project locally.


### 1. Clone the repository
First, clone the repository to your local machine using the following command:
```
git clone https://github.com/almusfuad/project_management_tool.git

cd project_management
```


### 2. Install Dependencies
Use the following command to install all the required dependencies:
```
pip install -r requirements.txt
```


### 3. Migrate the Database 
Run the following command to migrate the database:
```
python manage.py migrate
```


### 4. Create a Superuser (optional)
If you want to create a superuser to access the Django admin interface, run:
```
python manage.py createsuperuser
```
Give the information after the above command run.



### 5. Run the Development Server

To run the development server, use
```
python manage.py runserver
```
Your project should now be accessible at http://127.0.0.1:8000


## API Documentation

You can access the full API documentation for this project here:
[API Documentation](http://127.0.0.1:8000/api/doc/)

