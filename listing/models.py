from django.db import models
from django.template.defaultfilters import slugify
from ckeditor.fields import RichTextField
from realtor.models import Realtor, Disclaimer
# Create your models here.


class Listing(models.Model):
    CHOICE = (('commercial', 'commercial'),
              ('business', 'business'))
    Type = models.CharField(max_length=20, default='business', choices=CHOICE)
    listing_id = models.IntegerField(unique=True)
    realtor = models.ForeignKey(Realtor, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=300)
    slug = models.SlugField(unique=True, max_length=500)
    image_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
    image_1 = models.ImageField(
        upload_to='photos/%Y/%m/%d/', blank=True)
    image_2 = models.ImageField(
        upload_to='photos/%Y/%m/%d/', blank=True)
    image_3 = models.ImageField(
        upload_to='photos/%Y/%m/%d/', blank=True)
    image_4 = models.ImageField(
        upload_to='photos/%Y/%m/%d/', blank=True)
    area = models.ForeignKey('Area', on_delete=models.DO_NOTHING, null=True)
    business_type = models.ForeignKey(
        'Business_Type', on_delete=models.DO_NOTHING, null=True)
    description = RichTextField(config_name='default')
    price = models.IntegerField()
    status = models.ForeignKey(
        'Status', on_delete=models.DO_NOTHING, null=False)
    is_published = models.BooleanField(default=True)
    disclaimer = models.ForeignKey(Disclaimer, on_delete=models.DO_NOTHING)
    finance = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def summary(self):
        return self.description[:50] + '...'

    def save(self, *args, **kwargs):
            # Newly created object, so set slug
        self.slug = slugify(self.title)
        super(Listing, self).save(*args, **kwargs)


class Business_Type(models.Model):
    business_type = models.CharField(max_length=100)
    business_type_slug = models.SlugField()
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.business_type

    def save(self, *args, **kwargs):
            # Newly created object, so set slug
        self.business_type_slug = slugify(self.business_type)
        super(Business_Type, self).save(*args, **kwargs)


class Area(models.Model):
    area = models.CharField(max_length=50)
    area_slug = models.SlugField()
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.area

    def save(self, *args, **kwargs):
            # Newly created object, so set slug
        self.area_slug = slugify(self.area)
        super(Area, self).save(*args, **kwargs)


class Status(models.Model):
    status = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.status
