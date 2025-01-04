from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from tasks.models import Task, Comment
from projects.models import Project
from tasks.serializers import TaskSerializer, CommentSerializer

# Create your views here.
class TaskViewSet(viewsets.ModelViewSet):
      """ViewSet for viewing and editing Task instances."""
      queryset = Task.objects.all()
      serializer_class = TaskSerializer
      permission_classes = [IsAuthenticated]


      def list(self, request, project_id=None):
            """
            Retreive a list of all tasks in a project.
            URL: /api/projects/{project_id}/tasks/
            """

            if project_id is not None:
                  self.queryset = self.queryset.filter(project=project_id)
                  serializer = self.serializer_class(self.queryset, many=True)
                  return Response(serializer.data)
            return Response({"message": "Project ID is required for tasks."}, status=400)
      

      def create(self, request, project_id=None):
            """
            Create a new task in a project.
            URL: /api/projects/{project_id}/tasks/
            """
            if project_id is not None:
                  try:
                        project = Project.objects.get(pk=project_id)
                  except Project.DoesNotExist:
                        return Response({"message": "Project not found."}, status=404)
                  

                  request.data['project'] = project.id
                  serializer = self.serializer_class(data=request.data)
                  if serializer.is_valid():
                        serializer.save()
                        return Response(serializer.data, status=201)
                  return Response(serializer.errors, status=400)
            return Response({"message": "Project ID is required for tasks."}, status=400)



class CommentViewSet(viewsets.ModelViewSet):
      """ViewSet for viewing and editing Comment instances."""
      queryset = Comment.objects.all()
      serializer_class = CommentSerializer
      permission_classes = [IsAuthenticated]


      def list(self, request, task_id=None):
            """
            Retreive a list of all comments on a pacific task.
            URL: /api/tasks/{task_id}/comments/
            """

            if task_id is not None:
                  self.queryset = self.queryset.filter(task=task_id)
                  serializer = self.serializer_class(self.queryset, many=True)
                  return Response(serializer.data)
            return Response({"message": "Task ID is required for comments."}, status=400)
      

      def create(self, request, task_id=None):
            """
            Create a new comment on a task.
            URL: /api/tasks/{task_id}/comments/
            """
            if task_id is not None:
                  try:
                        task = Task.objects.get(pk=task_id)
                  except Task.DoesNotExist:
                        return Response({"message": "Task not found."}, status=404)
                  

                  request.data['task'] = task.id
                  serializer = self.serializer_class(data=request.data)
                  if serializer.is_valid():
                        serializer.save()
                        return Response(serializer.data, status=201)
                  return Response(serializer.errors, status=400)
            return Response({"message": "Task ID is required for comments."}, status=400)



