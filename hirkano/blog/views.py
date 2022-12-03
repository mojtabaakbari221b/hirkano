from django.views.generic.base import TemplateView
from .models import (
    SlideShow,
    Service,
)


class IndexView(TemplateView):
    template_name = 'blog/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context.update({
            'slide_showes' : SlideShow.objects.all(),
            'services' : Service.objects.all(),
        })

        return context
