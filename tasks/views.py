from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from tasks.models import Task, Comment
from tasks.serializers import TaskSerializer, CommentSerializer

# Create your views here.
class TaskViewSet(viewsets.ModelViewSet):
      """ViewSet for viewing and editing Task instances."""
      queryset = Task.objects.all()
      serializer_class = TaskSerializer
      permission_classes = [IsAuthenticated]



class CommentViewSet(viewsets.ModelViewSet):
      """ViewSet for viewing and editing Comment instances."""
      queryset = Comment.objects.all()
      serializer_class = CommentSerializer
      permission_classes = [IsAuthenticated]