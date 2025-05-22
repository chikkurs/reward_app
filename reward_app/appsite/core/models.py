from django.db import models
from django.contrib.auth.models import User

class App(models.Model):
    app_name = models.CharField(max_length=100)
    app_link = models.TextField(default="test")
    icon = models.ImageField(upload_to='apps/')
    category = models.CharField(max_length=100)
    sub_category = models.CharField(max_length=100)
    points = models.IntegerField(default=100)
    created_at = models.DateTimeField(auto_now_add=True)

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    app = models.ForeignKey(App, on_delete=models.CASCADE)
    screenshot = models.ImageField(upload_to='screenshots/')
    is_completed = models.BooleanField(default=False)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    points = models.IntegerField(default=100)

    def __str__(self):
        return f'{self.user.username} - {self.app.name}'
