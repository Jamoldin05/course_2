from django.contrib import admin
from .models import Subject,Course,Teacher

admin.site.register(Teacher)
admin.site.register(Subject)
admin.site.register(Course)
