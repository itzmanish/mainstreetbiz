from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
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
    youtube = models.URLField(blank=True, null=True)

    def __str__(self):
        return 'Social Links'

    # def clean(self):
    #     validate_only_one_instance(self)


class Contact(models.Model):
    address = RichTextField()
    phone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(null=True, blank=True)

    def __str__(self):
        return 'Contact Section of footer'

    # def clean(self):
    #     validate_only_one_instance(self)


class Home(models.Model):
    homepage = RichTextUploadingField(
        config_name='default', default='here some heading will go..')
    sellerbox_title = models.CharField(
        blank=True, default='I\'m a Seller', max_length=30)
    sellerbox_subtitle = RichTextField(
        blank=True, default='Discover how much property sold for with our comprehensive house price data.')
    sellerbox_button = models.CharField(
        default='Selling Transaction ', max_length=30)
    buyerbox_title = models.CharField(
        blank=True, default='I\'m a Buyer', max_length=30)
    buyerbox_subtitle = RichTextField(
        blank=True, default='Ensure you find the right home, near the right school with new School Checker tool.')
    buyerbox_button = models.CharField(
        default='Buying Transaction ', max_length=30)

    def __str__(self):
        return 'Home section'

    # def clean(self):
    #     validate_only_one_instance(self)


class About(models.Model):
    about = RichTextUploadingField(config_name='default')
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.created_at)


class BuyingProcess(models.Model):
    buying = RichTextField(config_name='default')
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.created_at)


class SellingProcess(models.Model):
    selling = RichTextUploadingField(config_name='default')
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.created_at)


class BusinessFinance(models.Model):
    business_finance = RichTextUploadingField(config_name='default')
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.created_at)
