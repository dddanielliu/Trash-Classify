from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # path('camera', views.camera, name='camera'),
    # path('upload/', views.upload_image, name='upload_image'),
    # path('success/', views.upload_success, name='success'),
    path('about/', views.about),
    path('images/<str:filename>/', views.serve_picture, name='serve_picture'),

    path('display/', views.display, name='display'),
    path('latest-image-data/', views.latest_image_data, name='latest_image_data'),  # For polling the latest image
    path('load-older-images/', views.load_older_images, name='load_older_images'),
]
