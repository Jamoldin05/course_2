from django.views.generic import ListView,DetailView
from .models import Course, Subject



class IndexView(ListView):
    model = Course
    template_name = "app/index.html"
    context_object_name = "courses"

    def get_queryset(self):
        return Course.objects.select_related('subject', 'owner')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['subjects'] = Subject.objects.all()
        return context



class CourseDetailView(DetailView):
    model = Course
    template_name = "app/detail.html"
    context_object_name = "course"
    slug_field = "slug"
    slug_url_kwarg = "slug"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['related_courses'] = Course.objects.filter(
            subject=self.object.subject
        ).exclude(id=self.object.id)[:6] 
        return context