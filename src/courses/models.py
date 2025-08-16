from django.db import models

# Create your models here.
class AccessTypes(models.TextChoices):
    ANYONE = 'anyone', 'Anyone'
    EMAIL_REQUIRED = 'email_required', 'Email Required'

class StatusTypes(models.TextChoices):
    DRAFT = 'draft', 'Draft'
    COMING_SOON = 'coming', 'Coming Soon'
    PUBLISHED = 'published', 'Published'

class Course(models.Model):
    title = models.CharField(max_length=144)
    description = models.TextField(null=True, blank=True)
    access = models.CharField(max_length=12, choices=AccessTypes.choices, default=AccessTypes.ANYONE)
    status = models.CharField(max_length=12, choices=StatusTypes.choices, default=StatusTypes.DRAFT)