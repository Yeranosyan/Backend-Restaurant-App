"""
URL configuration for littlelemon project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
#update URLConf by including URL patterns of restaurant app
from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from restaurant.views import BookingViewSet

# Inside the project-level urls.py file, call the router.register() function to register the ViewSets, and add the router.urls in the project's urlpatterns list. The app/urls.py file isn't needed for this.

router = DefaultRouter()
router.register(r'tables', BookingViewSet)
def redirect_view(request):
    return redirect('/restaurant/')

urlpatterns = [
    path('', redirect_view),
    path("admin/", admin.site.urls),
    path("restaurant/", include('restaurant.urls')),
    path("restaurant/booking/", include(router.urls)),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
]