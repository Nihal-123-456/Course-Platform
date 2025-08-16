from django.db import models

# Create your models here.
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
    image = models.ImageField(upload_to=image_upload_path, null=True, blank=True)
    access = models.CharField(max_length=7, choices=AccessTypes.choices, default=AccessTypes.EMAIL_REQUIRED)
    status = models.CharField(max_length=7, choices=StatusTypes.choices, default=StatusTypes.DRAFT)