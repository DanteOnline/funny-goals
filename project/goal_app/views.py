from django.shortcuts import render, get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Category, Goal

class CategoryListView(ListView):
    template_name = 'category_list.html'
    model = Category


class GoalListView(ListView):
    template_name = 'goal_list.html'
    model = Goal

    def get(self, request, *args, **kwargs):
        self.category = get_object_or_404(Category, pk=kwargs.get('category_id'))
        self.goal_time = kwargs.get('goal_time')
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(*kwargs)
        context['category'] = self.category
        context['tm'] = self.goal_time
        return context

    def get_queryset(self):
        qs = Goal.objects.filter(category = self.category, by_time=self.goal_time)
        return qs

class GoalDetailView(DetailView):
    model = Goal
    template_name = 'goal.html'