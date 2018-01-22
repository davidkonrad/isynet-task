from django.db import models

# Create your models here.
class TodoItem(models.Model):
    id = models.AutoField(primary_key=True)
    created_timestamp = models.DateTimeField(auto_now_add=True)
    solved_timestamp = models.DateTimeField(null=True, blank=True)
    title = models.CharField(max_length=127)
    description = models.CharField(max_length=2048)
    readonly_fields=('created_timestamp', )
    #admin
    def __str__(self):
        return self.title


