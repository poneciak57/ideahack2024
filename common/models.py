from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class CustomUser(AbstractUser):
    links = ArrayField(models.CharField(max_length=200), blank=True, default=list)

    def __str__(self):
        return self.username

class Profile(models.Model):
    PROFILE_TYPE_CHOICES = [
        ('scientist', 'Scientist'),
        ('businessman', 'Businessman'),
        ('investor', 'Investor'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # Can be either 'scientist' or 'businessman' or 'investor'
    type = models.CharField(max_length=100, choices=PROFILE_TYPE_CHOICES)
    open_for_contact = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.user.username} - {self.user.email}'

class Paper(models.Model):
    def get_default_author():
        return Profile.objects.get(user__username='biznes_user').id
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, default=get_default_author)
    title = models.CharField(max_length=100)
    brief = models.TextField()
    link = models.CharField(max_length=200)
    publication_date = models.DateField(auto_now_add=True)
    embedding = ArrayField(models.FloatField(), blank=True, default=list)
    def __str__(self):
        return f'{self.title}'

class Project(models.Model):
    PROJECT_TYPE_CHOICES = [
        ('startup', 'Startup'),
        ('working business', 'Working Business'),
        ('research', 'Research'),
    ]

    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    is_public = models.BooleanField(default=True)
    title = models.CharField(max_length=100)
    content = models.TextField()
    required_money = models.FloatField()
    type = models.CharField(max_length=20, choices=PROJECT_TYPE_CHOICES)
    brief = models.TextField()
    project_scope = models.TextField()
    profiles = models.ManyToManyField(Profile, related_name='projects')
    embedding = ArrayField(models.FloatField(), blank=True, default=list)

    def __str__(self):
        return f'{self.title}'

class FinanceRound(models.Model):
    title = models.CharField(max_length=100)
    brief = models.TextField()
    fundings_gathered = models.FloatField()
    end_date = models.DateField()
    start_date = models.DateField(auto_now_add=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

class Invitation(models.Model):
    INVITATION_STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
    ]

    sender = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='sender')
    receiver = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='receiver')
    status = models.CharField(max_length=100, choices=INVITATION_STATUS_CHOICES)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    message = models.TextField()

    def __str__(self):
        return f'{self.sender.user.username} -> {self.receiver.user.username} - {self.status} to {self.project.title}'
