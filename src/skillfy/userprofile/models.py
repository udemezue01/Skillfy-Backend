from django.db import models

from django.conf import settings
# Create your models here.


class Profile(models.Model):

    user                    =   models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    company_name             =  models.CharField(max_length = 3000, blank  = True)
    username                =   models.CharField(max_length=3000, unique=True , blank = True, null = True)
    bio                     =   models.CharField(max_length=3000, blank = True, null = True)

    website                 =   models.CharField(max_length=3000, null = True)
    twitter                 =   models.CharField(max_length=3000, blank = True)


    def __str__(self):

        return f'user.full_name'