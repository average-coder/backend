from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError 
# Create your models here.

class PostRequest(models.Model):
    date_posted  = models.DateTimeField(default=timezone.now, null = False, blank = False)
    data = models.TextField(null = False, blank = False)

class Feedback(models.Model):

    def ck_rating(value):
        if value>=0 and value<=5:
            return value
        elif value==None:
            return value
        else:
            raise ValidationError("Provide a valid rating value.")
            
    date_posted  = models.DateTimeField(default=timezone.now, null = False, blank = False)
    data = models.TextField(null = False, blank = False)
    rating = models.IntegerField(null = True, blank = True, validators=[ck_rating])
    


