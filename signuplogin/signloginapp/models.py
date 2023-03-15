from django.db import models


class Userlogin(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=50)

    def __str__(self) -> str:
        return str(self.id) + " " + self.name + " " + self.email
