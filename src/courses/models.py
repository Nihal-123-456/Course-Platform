from django.db import models
import helpers
from cloudinary.models import CloudinaryField
# Create your models here.

helpers.cloudinary_init() # initializing the cloudinary config

class AccessTypes(models.TextChoices):
    ANYONE = 'any', 'Anyone'
    EMAIL_REQUIRED = 'email', 'Email Required'

class StatusTypes(models.TextChoices):
    DRAFT = 'draft', 'Draft'
    COMING_SOON = 'soon', 'Coming Soon'
    PUBLISHED = 'publish', 'Published'

def image_upload_path(instance, filename):
    return f"{filename}"

class Course(models.Model):
    title = models.CharField(max_length=144)
    description = models.TextField(null=True, blank=True)
    image = CloudinaryField("image", null=True, blank=True)
    access = models.CharField(max_length=7, choices=AccessTypes.choices, default=AccessTypes.EMAIL_REQUIRED)
    status = models.CharField(max_length=7, choices=StatusTypes.choices, default=StatusTypes.DRAFT)

    @property
    def admin_image_url(self):
        if not self.image:
            return ""
        image_options = {
            "width": 200
        }
        url = self.image.build_url(**image_options) # creating the image url with the necessary options
        # self.image.image(**image_options) would return a html image tag containing the image url
        # self.image.build_url and self.image.image are part of the cloudinary package
        return url