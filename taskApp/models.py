from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.core.exceptions import ValidationError
from datetime import datetime
# Create your models here.

class UserCustom(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)

    profile_pic=models.ImageField(upload_to='profile_pics',blank=True)

    def __str__(self):
        return self.user.username   #user os object defined above



class UserTask(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    label=models.CharField(max_length=264)
    date=models.DateField()
    status=models.BooleanField(default=False)

    # def save(self, *args, **kwargs):
    #     if str(self.date)<datetime.today().strftime('%Y-%m-%d'):
    #         raise ValidationError("The date cannot be in the past!")
    #     super(UserTask, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.label)
