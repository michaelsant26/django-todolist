from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    
    # field task name in here
    task_name = models.CharField(max_length = 200)
    
    # field status done in here
    status = models.BooleanField(default = False)
    
    # field user
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    
    def __str__(self):
        return self.task_name