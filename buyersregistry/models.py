from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


class Register(models.Model):
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    business_type = models.CharField(max_length=50)
    investment_type = models.CharField(max_length=50)
    business_area = models.CharField(max_length=50)
    business_price = models.IntegerField()
    max_cash = models.IntegerField()
    remarks = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name + self.last_name


class BuyersDirectoryPage(models.Model):
    buyers_directory_page = RichTextUploadingField()
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.created_at)
