
from django.db import models
from django.conf import settings

# Create your models here.


class Post(models.Model):

    user                =   models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text                =   models.CharField(max_length=3000, blank =True)
    image               =   models.FileField(blank = True)
    created_at          =   models.DateTimeField(auto_now =False , auto_now_add=True)


    def __str__(self):

        return f'self.user.full_name'



class Comment(models.Model):

    user                =   models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    text                =   models.CharField(max_length=3000, blank = True, null = True)
    created_at          =   models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):

        return f'self.user.full_name'
