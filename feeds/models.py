from django.db import models

# Create your models here.


class FeedUrl(models.Model):
    site_name = models.CharField(max_length=200)
    site_url = models.URLField()
    added_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.site_name


class FeedPost(models.Model):
    title = models.CharField(max_length=200)
    link = models.CharField(max_length=2048)
    desc = models.TextField(null=True, blank=True)
    date = models.DateTimeField()

    def __str__(self):
        return self.title
