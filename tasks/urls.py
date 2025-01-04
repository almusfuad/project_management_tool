from django.urls import path, include
from tasks.views import TaskViewSet, CommentViewSet


urlpatterns = [
      path("tasks/<int:task_id>/comments/", CommentViewSet.as_view({"get": "list", "post": "create"}), name="task_comments"),
      path("comments/<int:comment_id>/", CommentViewSet.as_view({"get": "retrieve", "put": "update", "delete": "destroy"}), name="comment_detail"),
     path("projects/<int:project_id>/tasks/", TaskViewSet.as_view({"get": "list", "post": "create"}), name="project_tasks"),
      path("tasks/<int:task_id>/", TaskViewSet.as_view({"get": "retrieve", "put": "update", "delete": "destroy"}), name="task_detail"),
]