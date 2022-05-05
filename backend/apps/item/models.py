from config.constants import *
from django.db import models
from cloudinary.models import CloudinaryField


class Item(models.Model):
    class Meta(object):
        db_table = 'item'

    name = models.CharField('Name', blank=False, null=False,
                            max_length=120, db_index=True, default='anonymous')
    status = models.CharField(
        'Status', blank=False, null=False, default='draft', max_length=50, db_index=True, choices=STATUS
    )
    price = models.DecimalField(
        'Price', blank=False, null=False, max_digits=11, decimal_places=2, default=99.99
    )
    image = CloudinaryField(
        'image', blank=True, null=True
    )
    created_at = models.DateTimeField(
        'Created Datetime', blank=True, auto_now_add=True
    )
    updated_at = models.DateTimeField(
        'Updated Datetime', blank=True, auto_now=True
    )
