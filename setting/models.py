from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
from django.core.exceptions import ValidationError


def validate_only_one_instance(obj):
    model = obj.__class__
    if (model.objects.count() > 0 and
            obj.id != model.objects.get().id):
        raise ValidationError("Can only create 1 %s instance" % model.__name__)


class SocialLink(models.Model):
    facebook = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)

    def __str__(self):
        return 'Social Links'

    def clean(self):
        validate_only_one_instance(self)


class Contact(models.Model):
    address = RichTextField()
    phone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(null=True, blank=True)

    def __str__(self):
        return 'Contact Section of footer'

    def clean(self):
        validate_only_one_instance(self)


class Home(models.Model):
    homepage_heading = models.CharField(
        max_length=150, blank=True, default='Buy Or Sell Your Business')
    homepage_subheading = RichTextField(
        default='Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam pretium elit id ligula mollis commodo. Fusce at quam turpis. Cras ornare bibendum dui, nec rutrum neque maximus non. Integer aliquam tempus quam in vulputate. Suspendisse ultrices eu tellus ac accumsan.',
        blank=True)
    sellerbox_subtitle = RichTextField(
        blank=True, default='Discover how much property sold for with our comprehensive house price data.')
    buyerbox_subtitle = RichTextField(
        blank=True, default='Ensure you find the right home, near the right school with new School Checker tool.')

    def __str__(self):
        return 'Home section'

    def clean(self):
        validate_only_one_instance(self)


class About(models.Model):
    about = RichTextField(config_name='default')
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.created_at)


class BuyingProcess(models.Model):
    buying = RichTextField(config_name='default')
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.created_at)
