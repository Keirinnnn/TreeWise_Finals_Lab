from django.urls import path
from .views import (HomePageView, AboutPageView,WikiDetailView, 
WikiListView, WikiCreateView, WikiUpdateView, WikiDeleteView, 
VideoUploadView, VideoListView, ContactPageView, ImageUploadView, 
ImageGalleryView, VideoDetailView)

urlpatterns = [
    path('', HomePageView.as_view(), name='Home'),
    path('About/', AboutPageView.as_view(), name='About'),
    path('Wiki/<int:pk>', WikiDetailView.as_view(), name='Wiki'),
    path('Add/', WikiListView.as_view(), name='Add'),
    path('Wiki/Create', WikiCreateView.as_view(), name='Wiki_create'),
    path('Wiki/<int:pk>/Edit', WikiUpdateView.as_view(), name='Wiki_update'),
    path('Wiki/<int:pk>/Delete', WikiDeleteView.as_view(), name='Wiki_delete'),
    path('Image/Upload', ImageUploadView.as_view(), name='Image_upload'),
    path('Image/', ImageGalleryView.as_view(), name='Image_gallery'),
    path('Video/Upload', VideoUploadView.as_view(), name='Video'),
    path('Videos/', VideoListView.as_view(), name='Video_list'),
    path('Video/<int:pk>/', VideoDetailView.as_view(), name='Video_comment'),
    path('Contact/', ContactPageView.as_view(), name='Contact'),

]