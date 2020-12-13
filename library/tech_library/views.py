from django.shortcuts import render, Http404
from tech_library.models import Developer, Theme, Topic
def home(request):
    page_title = "Home" 
    content = "In this site we ..."

    return render(request, 'tech_library/home.html', locals())


def display_dev(request):
    developers  = Developer.objects.all()
    page_title = "Developers" 
    content = "List of developers:"
    if not developers:
        raise Http404
    return render(request, 'tech_library/developers.html', locals())