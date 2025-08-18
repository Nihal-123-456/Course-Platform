from .models import Course, Lesson, StatusTypes
from django.http import Http404

def get_course_list():
    qs = Course.objects.filter(status__in=[StatusTypes.PUBLISHED, StatusTypes.COMING_SOON])
    return qs

def get_course_detail(course_id):
    try:
        obj = Course.objects.get(slug_id=course_id, status__in=[StatusTypes.PUBLISHED, StatusTypes.COMING_SOON])
    except:
        raise Http404
    return obj

def get_lesson_detail(course_id, lesson_id):
    try:
        obj = Lesson.objects.get(slug_id=lesson_id, course__slug_id=course_id, status__in=[StatusTypes.PUBLISHED, StatusTypes.COMING_SOON], course__status__in=[StatusTypes.PUBLISHED, StatusTypes.COMING_SOON])
    except:
        raise Http404
    return obj