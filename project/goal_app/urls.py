from django.conf.urls import url
from .views import CategoryListView, GoalListView, GoalDetailView


urlpatterns = [
    url(r'^category/list/$', CategoryListView.as_view(), name='category_list'),
    url(r'^goal/list/(?P<category_id>\d+)/(?P<goal_time>\w{2})/$', GoalListView.as_view(), name='goal_list'),
    url(r'goal/detail/(?P<pk>\d+)$', GoalDetailView.as_view(), name='goal')
]