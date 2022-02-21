from django.db import models

# Create your models here.
class crud(models.Model):
    name=models.CharField(blank=True, null=True, max_length=50)

    def __str__(self) -> str:
        return self.name

class Addage(models.Model):

    age = models.IntegerField(blank=True, null=True)

    def __str__(self) -> str:

        return self.age