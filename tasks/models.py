from django.db import models

class Task(models.Model):
    task = models.CharField(max_length=500)
    date = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.task
    
