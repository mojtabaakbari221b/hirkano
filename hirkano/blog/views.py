from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from constance import config
from .models import (
    SlideShow,
    Service,
    Selected_Title,
    Projects,
    Person,
    HappyClient,
    Blog,
    Message,
    Specialty,
)


class ContextMixin :
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        context.update({
            'specialities': Specialty.objects.all(),
            'slide_showes' : SlideShow.objects.all(),
            'services' : Service.objects.all(),
            'selected_title': Selected_Title.objects.all(),
            'projects': Projects.objects.all(),
            'persons': Person.objects.all(),
            'happy_clinets': HappyClient.objects.all(),
            'blogs': Blog.objects.all(),
            'message': Message.objects.all(),
            'config': config,
        })

        return context

class IndexView(ContextMixin, CreateView):
    template_name = 'blog/index.html'
    model = Message
    fields = [
        'name',
        'email',
        'title',
        'message',
    ]
    success_url = reverse_lazy('index')

