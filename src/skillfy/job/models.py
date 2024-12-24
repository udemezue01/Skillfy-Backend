
from django.db import models
from django.conf import settings

# Create your models here.


class Job(models.Model):

    user               			=   models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title               		=   models.CharField(max_length=3000, blank =True)
    description              	=  	models.CharField(blank  = True, max_length = 3000)
    location                    =   models.CharField(blank = True, max_length = 3000)
    salary					 	=  	models.CharField(max_length = 3000, blank  = True)
    created_at        		 	=   models.DateTimeField(auto_now =False , auto_now_add=True)


    def __str__(self):

        return f'self.user.full_name'


