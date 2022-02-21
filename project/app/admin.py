import imp
from django.contrib import admin
from .models import crud,Addage
# Register your models here.
admin.site.register(crud),
admin.site.register(Addage)