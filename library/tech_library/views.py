from django.shortcuts import render, Http404

def home(request):
    page_title = "Home" 
    content = "In this site we ..."
    menu = {"Developers":"developers","Tech Field":"tech_field","Home":""}
    if not menu:
        raise Http404
    return render(request, 'tech_library/home.html', locals())

