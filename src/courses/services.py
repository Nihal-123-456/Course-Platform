from .models import Course, Lesson, StatusTypes
from django.http import Http404

def get_course_list():
    qs = Course.objects.filter(status__in=[StatusTypes.PUBLISHED, StatusTypes.COMING_SOON]) # to get the courses which are both published and coming soon
    return qs

def get_course_detail(course_id):
    try:
        obj = Course.objects.get(slug_id=course_id, status__in=[StatusTypes.PUBLISHED, StatusTypes.COMING_SOON])
    except:
        raise Http404
    return obj

def get_lesson_detail(course_id, lesson_id):
    try:
        # we use double underscores (__) to access the attributes of a foreignkey within the model
        obj = Lesson.objects.get(slug_id=lesson_id, course__slug_id=course_id, status__in=[StatusTypes.PUBLISHED, StatusTypes.COMING_SOON], course__status__in=[StatusTypes.PUBLISHED, StatusTypes.COMING_SOON])
    except:
        raise Http404
    return obj