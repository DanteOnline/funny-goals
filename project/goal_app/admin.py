from django.contrib import admin
from .models import Category, Goal


class GoalAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_success', 'by_time', 'by_type', 'category', 'in_control', 'has_refs_in_control', 'is_personal']


admin.site.register(Goal, GoalAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'in_future','priority']
    ordering = ['priority']
admin.site.register(Category, CategoryAdmin)
