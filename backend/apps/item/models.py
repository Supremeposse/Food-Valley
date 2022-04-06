from django.db import models
from cloudinary.models import CloudinaryField


class Item(models.Model):
    class Meta(object):
        db_table = 'item'

        name = models.CharField('Name', blank=False, null=False,
                                max_length=20, db_index=True, default='anonymous')
