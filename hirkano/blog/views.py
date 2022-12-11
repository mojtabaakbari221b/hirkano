from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .form import MessageForm
from .models import (
    SlideShow,
    Service,
    Selected_Title,
    Projects,
    Person,
    Happy_Client,
    Blog,
    Contant_Us,
    Message,
)
from .form import(
    MessageForm,
)


class ContextMixin :
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
   
        
        context.update({
            'slide_showes' : SlideShow.objects.all(),
            'services' : Service.objects.all(),
            'selected_title': Selected_Title.objects.all(),
            'projects': Projects.objects.all(),
            'persons': Person.objects.all(),
            'happy_client':Happy_Client.objects.all(),
            'blogs':Blog.objects.all(),
            'contant_us':Contant_Us.objects.all(),
            'message':Message.objects.all(),
            'form': MessageForm,
        })

        return context

class IndexView(ContextMixin, CreateView):

    template_name = 'blog/index.html'
    model = Message
    fields = ['name', 'email', 'title', 'message']
    
    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)
