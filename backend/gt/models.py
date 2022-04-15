from django.db import models

# Create your models here.
class Gt(models.Model):
    title = models.CharField(max_length=120)
    destination = models.TextField()
    path = models.CharField(max_length=200)

    def _str_(self):
        return self.title