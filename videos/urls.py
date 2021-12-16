from django.urls import path
from django.urls.resolvers import URLPattern

from . import views

app_name = "videos"

urlpatterns = [
    path('video/<int:id>/', views.video, name='video'),
    path('add_video/', views.add_video, name='add_video'),
    path('comment/', views.comment, name='comment'),
    path('remove/', views.remove, name='remove'),
    path('edit_video/<int:id>/', views.edit_video, name='edit_video'),
    path('delete/<int:id>/', views.delete, name='delete')
]
