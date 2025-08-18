from django.db import models
from cloudinary.models import CloudinaryField
from helpers import cloudinary_init, get_public_id_prefix, generate_slug_id, get_display_name
# Create your models here.

cloudinary_init() # initializing the cloudinary config

class AccessTypes(models.TextChoices):
    ANYONE = 'any', 'Anyone'
    EMAIL_REQUIRED = 'email', 'Email Required'

class StatusTypes(models.TextChoices):
    DRAFT = 'draft', 'Draft'
    COMING_SOON = 'soon', 'Coming Soon'
    PUBLISHED = 'publish', 'Published'

class Course(models.Model):
    title = models.CharField(max_length=144)
    # we use db_index to speed up the process of lookup through the slug_id
    slug_id = models.CharField(max_length=160, null=True, blank=True, db_index=True) 
    description = models.TextField(null=True, blank=True)

    image = CloudinaryField("image", null=True, blank=True, public_id_prefix=get_public_id_prefix, display_name=get_display_name, tags=['courses', 'timestamp'])

    access = models.CharField(max_length=7, choices=AccessTypes.choices, default=AccessTypes.EMAIL_REQUIRED)
    status = models.CharField(max_length=7, choices=StatusTypes.choices, default=StatusTypes.DRAFT)

    def save(self, *args, **kwargs):
        if self.slug_id == "" or self.slug_id is None:
            self.slug_id = generate_slug_id(self)
        super().save(*args, **kwargs)
    
    def get_display_name(self):
        return f"{self.title} - course"
    
    def is_coming_soon(self):
        return self.status == StatusTypes.COMING_SOON
    
    @property
    def path(self):
        if self.slug_id:
            return f"/course/{self.slug_id}"
        return None

class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=144)
    slug_id = models.CharField(max_length=160, null=True, blank=True, db_index=True)
    description = models.TextField(null=True, blank=True)

    image = CloudinaryField("image", null=True, blank=True, public_id_prefix=get_public_id_prefix, display_name=get_display_name, tags=['thumbnail', 'lesson'])
    # the video will be private by default
    video = CloudinaryField("video", type="private", null=True, blank=True, resource_type="video", public_id_prefix=get_public_id_prefix, display_name=get_display_name, tags=['videos', 'lesson'])

    can_preview = models.BooleanField(default=False, help_text="If the user does not have access to the course, can they preview this lesson?")
    status = models.CharField(max_length=7, choices=StatusTypes.choices, default=StatusTypes.PUBLISHED)

    updated_at = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if self.slug_id == "" or self.slug_id is None:
            self.slug_id = generate_slug_id(self)
        super().save(*args, **kwargs)
    
    def get_display_name(self):
        return f"{self.title} - {self.course.get_display_name()}"
    
    @property
    def is_coming_soon(self):
        return self.status == StatusTypes.COMING_SOON
    
    @property
    def has_video(self):
        return self.video is not None
 
    @property
    def path(self):
        course_path = self.course.path
        if self.slug_id:
            return f"{course_path}/lesson/{self.slug_id}"
        return None