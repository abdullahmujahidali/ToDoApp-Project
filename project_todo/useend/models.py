from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Task(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    title = models.CharField(max_length=250)
    description = models.TextField(null=False,blank=False)
    priority = models.CharField(max_length=6)
    complete = models.BooleanField(default=False)
    when_created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title

    class Meta:
        ordering = ['complete']
    