from django.shortcuts import render
from .models import Subject,Course


def index(request):
    subjects = Subject.objects.all()
    courses = Course.objects.all()

    context = {
        'subjects' : subjects,
        'courses' : courses
    }
    return render(request,'app/index.html',context)
