from django.urls import path

from example.views.example import example_view

urlpatterns = [
    path('', example_view, name="example-view")
]
