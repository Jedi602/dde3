from django.db import models
from django.db import models

class Todo(models.Model):
    srno = models.AutoField(primary_key=True, auto_created=True)
    task = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.task
