from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Task(models.Model):
    3
    GENDER_CHOICES = (
    ('H', 'High'),
    ('M', 'Medium'),
    ('L','Low')
    )

    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    title = models.CharField(max_length=250)
    description = models.CharField(max_length=250,null=False,blank=False)
    priority = models.CharField(choices=GENDER_CHOICES, max_length=128)
    complete = models.BooleanField(default=False)
    when_created = models.DateTimeField(auto_now_add=True)


   

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['priority']
    