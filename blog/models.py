from django.db import models

from cloudinary.models import CloudinaryField

# Create your models here.

class Tweet(models.Model):
    class Meta(object):
        db_table = 'tweet'

    name = models.CharField(
        'Name', max_length=20, blank=False, null=False)
    text = models.CharField(
        'Text', max_length=280, blank=False, null=False)
    image = CloudinaryField('image', blank= True, null= True)
    like_count = models.PositiveIntegerField(default=0, blank=True)
    created_at = models.DateField(
        'Created DateTime', blank=True, auto_now_add=True)
    updated_at = models.DateField(
        'Updated DateTime', blank=True, auto_now_add=True)