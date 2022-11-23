from django.shortcuts import render

# Create your views here.
def base(request):
    return render(request, 'base.html')

def blog_detail(request):
    return render(request, 'blog_detail.html')

def blog_list(request):
    return render(request, 'blog_list.html')
