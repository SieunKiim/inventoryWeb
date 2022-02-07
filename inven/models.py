from datetime import datetime

from django.db import models


# Create your models here.
class User(models.Model):  # 사용자
    name = models.CharField(max_length=200)
    department = models.CharField(max_length=200)
    position = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Tool(models.Model):  # 장비
    tool_name = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return "\'" + self.user.name + "\'의 " + self.tool_name
        # return self.tool_name


class Computer(models.Model):
    tool = models.ForeignKey(Tool, on_delete=models.CASCADE)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    OS = models.CharField(null=True, max_length=200)
    CPU = models.CharField(null=True, max_length=200)
    RAM = models.CharField(null=True, max_length=200)

    VGA = models.CharField(null=True, max_length=200)
    SSD_HDD = models.CharField(null=True, max_length=200)

    def __str__(self):
        return "\'" + self.tool.user.name + "\'의 " + self.tool.tool_name + "(" + self.OS + " | " + self.CPU + " | " + self.RAM + ")"


class Screen(models.Model):
    tool = models.ForeignKey(Tool, on_delete=models.CASCADE)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    size = models.CharField(null=True, max_length=200)
    brand = models.CharField(null=True, max_length=200)
    resolution = models.CharField(null=True, max_length=200)  # 해상도 (--- x ---) 으로 표현

    def __str__(self):
        return "\'" + self.tool.user.name + "\'의 " + self.tool.tool_name + "(" + self.brand + ")"


class Medical(models.Model):
    tool = models.ForeignKey(Tool, on_delete=models.CASCADE)
    medical_type = models.CharField(null=True, max_length=200)
    details = models.CharField(null=True, max_length=1000)
    serial_Number = models.CharField(null=True, max_length=30)
    man_date = models.DateField(default=datetime.now, blank=True)   # 생산 년도 (manufactured date)

    def __str__(self):
        return self.medical_type


class Others(models.Model):
    tool = models.ForeignKey(Tool, on_delete=models.CASCADE)
    other_tool_name = models.CharField(null=True, max_length=200)   # 기타 장비 이름
    details = models.CharField(null=True, max_length=1000)  # 세부 사항

    def __str__(self):
        return self.other_tool_name
