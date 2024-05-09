from django.urls import path
from . import views

urlpatterns = [
    path('manage-videos/', views.UploadVideo, name='manage-videos'),
    path('', views.VideoList, name='videolist'),
    path('<int:pk>/delete', views.DeleteVideo, name='video-delete'),
    # path('playlist/<int:pk>/', views.PlayListView, name='playlist_detail'),
    # path('<int:pk>/update', UpdateVideo.as_view(), name='video-update'),
    
]