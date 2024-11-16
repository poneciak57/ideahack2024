from django.contrib import admin

from .models import Profile, Paper, CustomUser, Project, Invitation

admin.site.register(Profile)
admin.site.register(Paper)
admin.site.register(CustomUser)
admin.site.register(Project)
admin.site.register(Invitation)