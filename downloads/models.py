from django.db import models


class Document(models.Model):
    thumb = models.ImageField(upload_to='documents/thumbs/')
    title = models.CharField(max_length=250)
    document = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    allow_download = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-uploaded_at',)


class FileUpload(models.Model):
    title = models.CharField(max_length=30, null=True)

    def __str__(self):
        return self.title


class DocumentUpload(models.Model):
    image = models.FileField(upload_to='documents/', null=True)
    title = models.ForeignKey(
        'FileUpload', on_delete=models.SET_NULL, null=True)
