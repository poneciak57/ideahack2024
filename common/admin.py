from django.contrib import admin

from .models import Profile, Paper, CustomUser, Project, Invitation, FinanceRound

admin.site.register(Profile)
admin.site.register(Paper)
admin.site.register(CustomUser)
admin.site.register(Project)
admin.site.register(Invitation)
admin.site.register(FinanceRound)