from django.urls import path, re_path
from aljoadmin import views

app_name = 'aljoadmin'
urlpatterns = [
    # Example: /aljo
    path('', views.AljoadminLV.as_view(), name='index'),
    # Example: /aljo/sort=likes
    path('sort=likes', views.AljoadminLikeLV.as_view(), name='likesort'),
    # Example: /aljo/starbucks/
    path('starbucks', views.AljoadminStarbucksLV.as_view(), name='starbucks'),
    # Example: /aljo/ediya/
    path('ediya', views.AljoadminEdiyaLV.as_view(), name='ediya'),
    # Example: /aljo/gongcha/
    path('gongcha', views.AljoadminGongchaLV.as_view(), name='gongcha'),
    # Example: /aljo/django-example/
    re_path(r'^(?P<slug>[-\w]+)/$', views.AljoadminDV.as_view(), name='detail'),
    # Example: /aljo/tag/tagname/
    path('tag/<str:tag>/', views.TaggedObjectLV.as_view(), name='tagged_object_list'),
    # Example: /aljo/like/django-example/
    re_path(r'^(?P<slug>[-\w]+)/like/$', views.like, name='like'),
    # Example: /aljo/search/
    #path('search', views.search, name='search'),
]