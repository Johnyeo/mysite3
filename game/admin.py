from django.contrib import admin

# Register your models here.
from .models import Goods, Character, Relationship

admin.site.register(Goods)
admin.site.register(Character)
admin.site.register(Relationship)