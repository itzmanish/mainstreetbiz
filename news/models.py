from django.db import models
from django.template.defaultfilters import slugify
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.


class News(models.Model):
    title = models.CharField(max_length=500)
    subtitle = models.CharField(max_length=500, blank=True)
    slug = models.SlugField(unique=True, max_length=500)
    content = RichTextUploadingField(config_name='default')
    image = models.ImageField(upload_to='images/news/')
    created_At = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def summary(self):
        return self.content[:50] + '...'

    def pretty_date(self):
        return self.created_At.strftime('%B %d , %Y')

    def save(self, *args, **kwargs):
            # Newly created object, so set slug
        self.slug = slugify(self.title)
        super(News, self).save(*args, **kwargs)


class ImageUpload(models.Model):
    title = models.CharField(max_length=30, null=True)

    def __str__(self):
        return self.title


class ImageUploadFile(models.Model):
    image = models.FileField(upload_to='images/news/', null=True)
    title = models.ForeignKey(
        'ImageUpload', on_delete=models.SET_NULL, null=True)
