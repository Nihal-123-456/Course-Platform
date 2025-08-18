from django.contrib import admin
from django.utils.html import format_html
from .models import Course,Lesson
import helpers
# Register your models here.

# to create stacked lesson model instances for adding them within the course model
class LessonInline(admin.StackedInline):
    model = Lesson
    extra = 0
    readonly_fields = ['slug_id']

class CourseAdmin(admin.ModelAdmin):
    inlines = [LessonInline] # to add the lesson model within the course model
    list_display = ['title', 'description']
    list_filter = ['status', 'access']
    readonly_fields = ['slug_id']

admin.site.register(Course, CourseAdmin)