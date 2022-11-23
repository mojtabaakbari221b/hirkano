from django.urls import path
from . import views


urlpatterns = [
    path('',views.base),
    path('detail/', views.blog_detail),
    path('list/', views.blog_list),
    path('skelector/',views.skelector)
    

]