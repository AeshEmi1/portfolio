from django.shortcuts import render
from django.views.decorators.cache import cache_control


@cache_control(public=True, max_age=600)
def index(request):
    return render(request, "index.html")


@cache_control(public=True, max_age=600)
def projects(request):
    return render(request, "projects.html")


@cache_control(public=True, max_age=600)
def contact(request):
    return render(request, "contact.html")
