from django.urls import path, re_path
from aljouser import views

app_name = 'aljouser'
urlpatterns = [
    # Example: /aljoPost
    path('', views.AljouserLV.as_view(), name='index'),
    # Example: /aljoPost/sort=likes
    path('sort=likes', views.AljouserLikeLV.as_view(), name='likesort'),
    # Example: /aljoPost/sort=mypost
    path('sort=mypost', views.AljouserMypostLV.as_view(), name='mypostsort'),
    # Example: /aljoPost/starbucks/
    path('starbucks', views.AljouserStarbucksLV.as_view(), name='starbucks'),
    # Example: /aljoPost/ediya/
    path('ediya', views.AljouserEdiyaLV.as_view(), name='ediya'),
    # Example: /aljoPost/gongcha/
    path('gongcha', views.AljouserGongchaLV.as_view(), name='gongcha'),
    # Example: /aljo/aljoPost/django-example/
    path('<int:pk>/', views.AljouserDV.as_view(), name='detail'),
    # Example: /aljoPost/tag/tagname/
    path('tag/<str:tag>/', views.TaggedObjectLV.as_view(), name='tagged_object_list'),
    # Example: /aljo/like/django-example/
    path('<int:pk>/like/', views.like, name='like'),

    path('new/add/', views.AljoCreateView.as_view(), name='add'),
    path('<int:pk>/update/', views.AljoUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', views.AljoDeleteView.as_view(), name='delete'),
]

