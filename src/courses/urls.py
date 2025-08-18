from django.urls import path
from .views import *

urlpatterns = [
    path('', course_list_view, name='published_courses'),
    path('<slug:course_id>/', course_detail_view, name='course_detail'),
    path('<slug:course_id>/lesson/<slug:lesson_id>/', lesson_detail_view, name='lesson_detail')
]
