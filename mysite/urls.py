"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include
from django.conf import settings
from mysite.views import HomeView, UserCreateView, UserCreateDoneTV, search, brand, brand2, brand3

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),  # 추가
    path('accounts/register/', UserCreateView.as_view(), name='register'),  # 추가
    path('accounts/register/done/', UserCreateDoneTV.as_view(), name='register_done'),  # 추가
    path('aljo/', include('aljoadmin.urls')),
    path('aljoPost/', include('aljouser.urls')),
    path('recommend/', include('recommend.urls')),
    path('', HomeView.as_view(), name='home'),
    path('search', search, name='search'),
    path('brand/starbucks', brand, name='brand'),
    path('brand/ediya', brand2, name='brand2'),
    path('brand/gongcha', brand3, name='brand3'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
