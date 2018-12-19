from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=30)
    phone = models.CharField(max_length=20)
    message = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class ContactSelling(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=30)
    phone = models.CharField(max_length=20)
    city = models.CharField(max_length=50)
    type_of_business = models.CharField(max_length=50)
    message = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class ContactModel(models.Model):
    listing_id = models.IntegerField()
    listing_title = models.CharField(max_length=500)
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=20, null=True, blank=True)
    message = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
