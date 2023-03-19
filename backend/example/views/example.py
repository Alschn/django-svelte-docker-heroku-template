from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.shortcuts import render


def example_view(request: WSGIRequest) -> HttpResponse:
    context = {
        "page_title": "django-svelte-template",
        "svelte_props": {
            "prop1": "Hello",
            "prop2": "World",
        }
    }

    return render(request, 'example/index.html', context)
