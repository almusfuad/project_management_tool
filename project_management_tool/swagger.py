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
            - Project: Represents a project with fields like name, description, created_at, updated_at, and owner (ForeignKey to User).
            - Task: Represents a task with fields like title, description, due_date, completed, project (ForeignKey to Project), assigned_to (ForeignKey to User), created_at, and updated_at.
            - Comment: Represents a comment with fields like task (ForeignKey to Task), author (ForeignKey to User), content, created_at, and updated_at.

            Relationships:
            - A Project can have multiple Tasks.
            - A Task can have multiple Comments.
            - A Task is assigned to a User.
            - A Comment is authored by a User.

            Output and Behavior:
            - JSON responses for all API endpoints.
            - Detailed error messages and status codes for invalid requests.
            - Comprehensive documentation of all available endpoints, including parameters and expected responses.

            JSON Format for Creating Objects (POST):
            - User:

                  - create: 
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

                  - create:          
                  {
                        "name": "Project Name",
                        "description": "Project Description",
                        "owner": The ID of the user who owns the project, 
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

                  - create:
                  {
                        "title": "Task Title",
                        "description": "Task Description",
                        "status": Can be "To Do", "In progress", or "Done",
                        "priority": Can be "Low", "Medium", or "High",
                        "project": The ID of the project the task belongs to (integer) -> 1,
                        "assigned_to": The ID of the user assigned to the task (integer) or null,
                        "projectMembers": List of User IDs who are part of the project -> [1, 2, 3]
                  }
            - Comment:

                  - create:
                  {
                        "task": Task ID(int) to which the comment is related -> 1,  
                        "author": User ID(it) of the author of the comment -> 2,
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