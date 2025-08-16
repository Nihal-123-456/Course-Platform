from django.contrib import admin
from django.utils.html import format_html
from .models import Course,Lesson
# Register your models here.

# to create stacked lesson model instances for adding them within the course model
class LessonInline(admin.StackedInline):
    model = Lesson
    extra = 0

class CourseAdmin(admin.ModelAdmin):
    inlines = [LessonInline] # to add the lesson model within the course model
    list_display = ['title', 'description']
    list_filter = ['status', 'access']
    readonly_fields = ['admin_image']

    def admin_image(self, obj, *args, **kwargs):
        url = obj.admin_image_url
        return format_html(f'<img src={url} />') # using the url to create a html element

admin.site.register(Course, CourseAdmin)