from django.db import models
from django.utils import timezone
from django.db.models.deletion import CASCADE


# Create your models here.

class Post(models.Model):
    autor = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField(default="")
    createdDate = models.DateTimeField(default=timezone.now)
    publishedDate = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.publishedDate = timezone.now()
        self.save()

    def __str__(self):
        return self.title