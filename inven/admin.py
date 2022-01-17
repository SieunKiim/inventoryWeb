from django.contrib import admin

# Register your models here.
from inven.models import Tools, Users

admin.site.register(Tools)
admin.site.register(Users)
