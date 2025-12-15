from django.urls import path
from .views import IndexView,CourseDetailView

app_name = 'app'


urlpatterns = [
    path("", IndexView.as_view(), name="home"),
    path("course/<slug:slug>/", CourseDetailView.as_view(), name="course_detail"),
]

