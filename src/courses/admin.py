from django.contrib import admin
from django.utils.html import format_html
from .models import Course
# Register your models here.
class CourseAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'admin_image']
    list_filter = ['status', 'access']
    readonly_fields = ['admin_image']

    def admin_image(self, obj, *args, **kwargs):
        url = obj.admin_image_url
        return format_html(f'<img src={url} />') # using the url to create a html element

admin.site.register(Course, CourseAdmin)