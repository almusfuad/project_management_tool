from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Project(models.Model):
      name = models.CharField(max_length=100)
      description = models.TextField()
      owner = models.ForeignKey(User, on_delete=models.CASCADE)
      created_at = models.DateTimeField(auto_now_add=True)

      def __str__(self):
              return self.name
      

class ProjectMember(models.Model):
      ROLE = (('Admin', 'Admin'), ('Member', 'Member'))

      project = models.ForeignKey(Project, on_delete=models.CASCADE)
      user = models.ForeignKey(User, on_delete=models.CASCADE)
      role = models.CharField(max_length=50, choices=ROLE)

      def __str__(self):
             return self.project.name + ' - ' + self.user.username + ' - ' + self.role