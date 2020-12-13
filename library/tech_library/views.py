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

def display_themes(request):
    themes  = Theme.objects.all()
    page_title = "Themes" 
    content = "List of Themes:"
    if not themes:
        raise Http404
    return render(request, 'tech_library/themes.html', locals())


def display_dev_details(request, id_dev):
    dev_details =Developer.objects.get(id=id_dev)
    topics = dev_details.topic_set.all()
    return render(request, 'tech_library/developer_details.html', locals())

def display_themes_details(request, id_theme):
    theme  = Theme.objects.get(id=id_theme)
    topics = list(theme.topic_set.all())

    return render(request, 'tech_library/theme_details.html', locals())


def display_topic_details(request, id_theme):
    topic  = Topic.objects.get(id=id_theme)
    devs = topic.developer.all()
    themes = topic.theme.all()
    return render(request, 'tech_library/topic_details.html', locals())



