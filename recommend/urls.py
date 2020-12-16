from django.urls import path
from recommend import views

app_name = 'recommend'
urlpatterns = [
    path('', views.recommend_index, name='recommend_index'),
    path('result/', views.recommend_result, name='recommend_result'),

]