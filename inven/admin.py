from django.contrib import admin

# Register your models here.
from inven.models import Tool, User, Computer, Screen

admin.site.register(Tool)
admin.site.register(User)
admin.site.register(Computer)
admin.site.register(Screen)
