"""
URL configuration for website project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path, include
# from trash_classify.views import home, about
# from trash_classify.views import serve_picture
# from trash_classify.views import image_view
# from trash_classify.views import success
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('trash_classify.urls')),
    # path('', home),
    # path('about/', about),
    # path('pics/<str:filename>/', serve_picture, name='serve_picture'),
    # path('image_upload', image_view, name='image_upload'),
    # path('success', success, name='success'),
    path('', include('pwa.urls')),
# ]
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

from django.http import HttpResponseForbidden
from django.conf.urls import handler404

handler404 = lambda request, exception: HttpResponseForbidden("Access forbidden: The URL you requested is not allowed.")
