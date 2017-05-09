from django.shortcuts import render
from django.views.generic.base import TemplateView


class IndexTemplateView(TemplateView):
    template_name = 'index.html'
