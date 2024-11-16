from django.contrib import admin

from .models import Profile, Paper, CustomUser

admin.site.register(Profile)
admin.site.register(Paper)
admin.site.register(CustomUser)