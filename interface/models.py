from django.db import models

# Create your models here.

class News(models.Model):
    title = models.CharField(max_length=200)
    text = models.CharField(max_length=500)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
