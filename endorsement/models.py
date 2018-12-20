from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


class Clients(models.Model):
    name = models.CharField(max_length=30)
    business_involved_in = models.CharField(max_length=200)
    location = models.CharField(max_length=50)
    comment = RichTextUploadingField(config_name='default')
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
