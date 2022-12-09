from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .form import MessageForm
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

        #if self.request.method == 'POST':
         #   form = MessageForm(self.request.POST)
          #  if form.is_valid:
           #     Message.objects.create(name=form.data['name'], email=form.data['email'], title=form.data['title'], message=form.data['message'])
            #else:
             #  pass

        context.update({
            'slide_showes' : SlideShow.objects.all(),
            'services' : Service.objects.all(),
            'selected_title': Selected_Title.objects.all(),
            'projects': Projects.objects.all(),
            'persons': Person.objects.all(),
            'blogs':Blog.objects.all(),
            'contant_us':Contant_Us.objects.all(),
            'message':Message.objects.all(),
            'form': MessageForm,
        })

        return context

class MessageCreateVeiw(LoginRequiredMixin, CreateView):
    model = Message
    fields = ['name', 'email', 'title', 'message']
    template_name = 'blog/index.html'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)
    

