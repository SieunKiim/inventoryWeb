from django.db import models


# Create your models here.
class User(models.Model):  # 사용자
    name = models.CharField(max_length=200)
    department = models.CharField(max_length=200)
    position = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Tool(models.Model):  # 장비
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    tool = models.CharField(max_length=200)

    def __str__(self):
        # "\'" + self.user.name + "\'의 " +
        return self.tool


class Computer(models.Model):
    tool = models.ForeignKey(Tool, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    OS = models.CharField(max_length=200)
    CPU = models.CharField(max_length=200)
    RAM = models.CharField(max_length=200)

    VGA = models.CharField(max_length=200)
    SSD_HDD = models.CharField(max_length=200)

    def __str__(self):
        return "\'" + self.user.name + "\'의 " + self.tool.tool + "(" + self.OS + " | " + self.CPU + " | " + self.RAM + ")"


class Screen(models.Model):
    tool = models.ForeignKey(Tool, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    size = models.CharField(max_length=200)
    brand = models.CharField(max_length=200)
    resolution = models.CharField(max_length=200)  # 해상도 (--- x ---) 으로 표현

    def __str__(self):
        return "\'" + self.user.name + "\'의 " + self.tool.tool + "(" + self.brand + ")"


class Medical(models.Model):
    tool = models.ForeignKey(Tool, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name