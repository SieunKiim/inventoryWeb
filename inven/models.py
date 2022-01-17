from django.db import models


# Create your models here.
class Users(models.Model):  # 사용자
    name = models.CharField(max_length=200)
    department = models.CharField(max_length=200)
    position = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Tools(models.Model):  # 장비
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    tool = models.CharField(max_length=200)

    def __str__(self):
        return self.tool


