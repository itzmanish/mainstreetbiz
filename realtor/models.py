from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.


class Realtor(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='realtors/')
    description = RichTextUploadingField(blank=True)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    joined_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Disclaimer(models.Model):
    disclaimer = RichTextUploadingField(config_name='default')
    created_by = models.ForeignKey('Realtor', on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.disclaimer[:20]


class LegalDisclaimer(models.Model):
    legal_disclaimer = RichTextUploadingField(config_name='default')
    created_by = models.ForeignKey('Realtor', on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.legal_disclaimer[:20]


class PrivacyPolicy(models.Model):
    privacy_policy = RichTextUploadingField(config_name='default')
    created_by = models.ForeignKey('Realtor', on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.privacy_policy[:20]
