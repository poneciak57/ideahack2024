from django.db import models
from django.contrib.postgres.fields import ArrayField

class Profile(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    # Can be either 'scientist' or 'businessman' or 'investor'
    type = models.CharField(max_length=100)
    open_for_contact = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.user.username} - {self.user.email}'

class Paper(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    brief = models.TextField()
    link = models.CharField(max_length=100)
    publication_date = models.DateField()
    embedding = ArrayField(models.FloatField(), blank=True, default=list)

    def __str__(self):
        return f'{self.title}'