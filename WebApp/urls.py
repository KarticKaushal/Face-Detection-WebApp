"""webapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path
from django.conf.urls import url, include
import face_detection
from face_detection import views                                                                                                                                                                                                                                                                                                                                                                                                                                    

urlpatterns = [
    
    path('face_detection/', include('face_detection.urls')),
    path('admin/', admin.site.urls),
    url(r'', include('face_detection.urls')),
    url(r'^dface/$', views.dface, name='dface'), #face_detection webapp
]   