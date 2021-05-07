from django.db import models

# Create your models here.
class Todo(models.Model):
    new_task = models.TextField(max_length=255)
    date = models.DateField(auto_now_add=True)


    def __str__(self):
        return self.new_task