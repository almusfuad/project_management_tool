from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
      openapi.Info(
            title="Project Management tools API",
            default_version="v1",
            description="""
            This is a simple API for managing projects, tasks, and teams. It allows users to create, update, delete, and view projects and tasks. 
            The API supports user authentication and authorization via JWT, ensuring secure access to resources. 

            
            Models Schema:
            - User: Represents a user with username(unique), email(unique), first_name, last_name, and password. 
            - Project: Represents a project with name, description, owner (ForeignKey to User), and created_at.
            - ProjectMember: Represents a member in a project with project (ForeignKey to Project), user (ForeignKey to User), and role (Admin/Member).
            - Task: Represents a task with title, description, status (To Do/In progress/Done), priority (Low/Medium/High), assigned_to (ForeignKey to User), project (ForeignKey to Project), created_at, and due_date.
            - Comment: Represents a comment with content, user (ForeignKey to User), task (ForeignKey to Task), and created_at.



            Relationships:
            - A User can own multiple Projects.
            - A Project can have multiple Tasks.
            - A Project can have multiple ProjectMembers.
            - A Task can have multiple Comments.
            - A Task is assigned to a User.
            - A Comment is authored by a User.

            
            Output and Behavior:
            - JSON responses for all API endpoints.
            - Detailed error messages and status codes for invalid requests.
            - Comprehensive documentation of all available endpoints, including parameters and expected responses.

            JSON Format for Creating Objects (POST):
            - User:

                  - register: 
                  {
                        "username": "new_user",
                        "email": "new_user@example.com",
                        "first_name": "First",
                        "last_name": "Last",
                        "password": "user_password"
                  }

                  - login: 
                  {
                        "username": "new_user",
                        "password": "user_password"
                  }
            - Project:
         
                  {
                        "name": "Project Name",
                        "description": "Project Description",
                        "owner": User ID of the owner, 
                        "members": [
                              {
                                    "user": User ID of the member,
                                    "role": "Admin"
                              },
                              {
                                    "user": Another user ID,
                                    "role": "Member"
                              }
                        ]
                  }
            - Task:

                  {
                        "title": "Task Title",
                        "description": "Task Description",
                        "status": "To Do"/"In progress"/"Done",
                        "priority": "Low"/"Medium"/"High",
                        "assigned_to": UserID(int) or null,
                        "projectMembers": List of User IDs -> [1, 2, 3]
                  }
            - Comment:

                  {  
                        "author": UserID(int) of comment author -> 2,
                        "content": "This is a comment on the task"
                  }
            """,
            terms_of_service="https://www.google.com/policies/terms/",
            contact=openapi.Contact(email="almusfuad@gmail.com"),
            license=openapi.License(name="BSD License"),
      ),
      public=True,
      permission_classes=(permissions.AllowAny,),
)