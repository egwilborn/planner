from django.contrib import admin

# Register your models here.

from .models import Todo, List

# Register your models here.
admin.site.register(Todo)
admin.site.register(List)
