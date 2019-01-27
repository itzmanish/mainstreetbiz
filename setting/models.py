from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor.fields import RichTextField


# Create your models here.
from django.core.exceptions import ValidationError


def validate_only_one_instance(obj):
    """ this will validate for only one instance of a choice of page """
    model = obj.__class__
    # Check for instance of page if it is already exist.
    items = model.objects.filter(page_name=obj.page_name)
    # Check if existing instance have the same id of that instance.

    def check_id(model, obj, items):
        try:
            ids = model.objects.get(page_name=obj.page_name)
        except model.DoesNotExist:
            ids = None
        # If existing instance have the same id which we want to add or update then return false.
        if items and ids:
            return obj.id != ids.id
        else:
            return False
    # I we get true return from function check_id raise a validation error so that instance can't be created.
    if check_id(model, obj, items):
        raise ValidationError(
            "This {0} instance with page name '{1}' is exists, so please add another or edit that page".format(model.__name__, obj.page_name))


class SocialLink(models.Model):
    facebook = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    youtube = models.URLField(blank=True, null=True)

    def __str__(self):
        return 'Social Links'


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
    buying = RichTextUploadingField(config_name='default')
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


class SellYourBusiness(models.Model):
    title = models.CharField(max_length=50)
    subtitle = RichTextField(config_name='default')

    def __str__(self):
        return self.title


class FooterImages(models.Model):
    name = models.CharField(max_length=100)
    link = models.URLField()
    image = models.ImageField(upload_to='images/footer_images', null=True)

    def __str__(self):
        return self.name


class MetaTags(models.Model):
    CHOICES = (('home', 'home'),
               ('our-team', 'our-team'),
               ('about-business', 'about-business'),
               ('buying-process', 'buying-process'),
               ('small-business-finance', 'small-business-finance'),
               ('business-listing', 'business-listing'),
               ('commercial-listing', 'commercial-listing'),
               ('blog', 'blog'),
               ('download', 'download'),
               ('selling-process', 'selling-process'),
               ('completed-deals', 'completed-deals'),
               ('sell-your-business', 'sell-your-business'),
               ('buyers-directory', 'buyers-directory'),
               ('buyers-directory-register', 'buyers-directory-register'),
               ('endorsements', 'endorsements'),
               ('news', 'news'),
               ('contact', 'contact'),
               )

    page_name = models.CharField(
        max_length=50, choices=CHOICES, default='home')
    meta_title = models.TextField()
    meta_description = models.TextField()
    meta_keywords = models.TextField()

    def __str__(self):
        return self.page_name

    def clean(self):
        validate_only_one_instance(self)
