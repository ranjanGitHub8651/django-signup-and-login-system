from django.db import models


class Userlogin(models.Model):
    GENDER = (
        ("MALE", "MALE"),
        ("FEMALE", "FEMALE"),
        (
            "OTHER",
            "OTHER",
        ),
    )
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, null=False)
    email = models.EmailField(max_length=255, null=True, default="")
    gender = models.CharField(max_length=100, choices=GENDER, default="MALE", null=False)
    username = models.CharField(max_length=255, null=False)
    password = models.CharField(max_length=50, null=False)

    # def __str__(self) -> str:
    #     return str(self.id) + " " + self.name + " " + self.email
