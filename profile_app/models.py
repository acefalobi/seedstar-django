from django.db import models


# Create your models here.


class Profile(models.Model):
    name = models.CharField(max_length=128)
    email = models.EmailField(max_length=128, unique=True)

    def __str__(self):
        return self.name + " (" + self.email + ")"
