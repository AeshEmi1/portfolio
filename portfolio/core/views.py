from django.shortcuts import render
from django.views.decorators.cache import cache_control
from django.utils.decorators import method_decorator


@method_decorator(
    cache_control(public=True, max_age=600),
    name="dispatch",
)
def index(request):
    return render(request, "index.html")


@method_decorator(
    cache_control(public=True, max_age=600),
    name="dispatch",
)
def projects(request):
    return render(request, "projects.html")


@method_decorator(
    cache_control(public=True, max_age=600),
    name="dispatch",
)
def contact(request):
    return render(request, "contact.html")
