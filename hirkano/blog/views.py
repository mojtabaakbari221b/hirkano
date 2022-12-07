from django.views.generic.base import TemplateView
from .models import (
    SlideShow,
    Service,
    Selected_Title,
    Projects,
    Person,
    Blog,
    Contant_Us,
    Message,
)
from .form import(
    MessageForm,
)


class IndexView(TemplateView):
    template_name = 'blog/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        print(self.request.user)

        context.update({
            'slide_showes' : SlideShow.objects.all(),
            'services' : Service.objects.all(),
            'selected_title': Selected_Title.objects.all(),
            'projects': Projects.objects.all(),
            'persons': Person.objects.all(),
            'blogs':Blog.objects.all(),
            'contant_us':Contant_Us.objects.all(),
            'message':Message.objects.all(),
            
        })

        return context
