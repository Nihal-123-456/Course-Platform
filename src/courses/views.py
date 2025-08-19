from django.shortcuts import render
from .models import StatusTypes
from .services import *
from helpers import cloudinary_video_processing

# Create your views here.
def course_list_view(request):
    qs = get_course_list()
    context = {
        'qs': qs,
    }
    return render(request, 'courses/course_list.html', context)

def course_detail_view(request, course_id):
    obj = get_course_detail(course_id)
    # we are accessing the lessons of a course through reverse relationship (modelNameInSmallCase_set)
    qs = obj.lesson_set.filter(status__in=[StatusTypes.PUBLISHED, StatusTypes.COMING_SOON]) 
    context = {
        'obj': obj,
        'qs': qs
    }
    return render(request, 'courses/course_detail.html', context)

def lesson_detail_view(request, course_id, lesson_id):
    obj = get_lesson_detail(course_id, lesson_id)
    context = {
        'obj': obj,
    }
    if not obj.is_coming_soon and obj.has_video:
        video_emd = cloudinary_video_processing(obj, width=1250)
        context['video_emd']=video_emd
        return render(request, 'courses/lesson_detail.html', context)
    return render(request, 'courses/coming_soon_lesson.html', context)