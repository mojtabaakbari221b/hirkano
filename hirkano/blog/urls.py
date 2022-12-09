from django.urls import path
from . import views
from .views import MessageCreateVeiw

urlpatterns = [
    path('', views.IndexView.as_view()),
    path('', MessageCreateVeiw.as_view())
]