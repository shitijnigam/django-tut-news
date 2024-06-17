from django.shortcuts import render
from django.views.generic import TemplateView

# path("", TemplateView.as_view(template_name="home.html"), name="home"),

# Create your views here.


class HomePageView(TemplateView):
    template_name = "home.html"
