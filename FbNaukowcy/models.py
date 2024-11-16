from django.db import models

class Publication(models.Model):
    title = models.CharField(max_length=200)
    brief = models.TextField()
    link =models.URLField(default='https://arxiv.org/abs/1706.03762')
    created_at = models.DateTimeField(auto_now_add=True)
    embedding = models.JSONField(default=dict) ###bedziemy to losować

    def __str__(self):
        return self.title