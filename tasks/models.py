from django.db import models
from django.contrib.auth.models import User
from projects.models import Project

# Create your models here.
class Task(models.Model):
      STATUS = (("To Do", "To Do"), ("In progress", "In progress"), ("Done", "Done"))
      PRIORITY = (("Low", "Low"), ("Medium", "Medium"), ("High", "High"))


      title = models.CharField(max_length=200)
      description = models.TextField()
      status = models.CharField(max_length=200, choices=STATUS)
      priority = models.CharField(max_length=200, choices=PRIORITY)
      assigned_to = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
      project = models.ForeignKey(Project, on_delete=models.CASCADE)
      created_at = models.DateTimeField(auto_now_add=True)
      due_date = models.DateTimeField(null=True, blank=True)


      def __str__(self):
            return self.title - self.project.title - self.assigned_to.username - self.status - self.priority
      


class Comment(models.Model):
      content = models.TextField()
      user = models.ForeignKey(User, on_delete=models.CASCADE)
      task = models.ForeignKey(Task, on_delete=models.CASCADE)
      created_at = models.DateTimeField(auto_now_add=True)


      def __str__(self):
            return self.content - self.user.username - self.task.title
