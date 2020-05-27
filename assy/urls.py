from django.urls import path, include
from . import views
from .views import HomeList, PostCreate, chat, PostDelete, ProfileUpdate

urlpatterns = [
    path('assy/home/', HomeList.as_view(), name='home'),
    path('assy/post/', PostCreate.as_view(), name='post'),
    #path('assy/post', views.create, name='post'),
    path('assy/chat/', views.chat, name='chat'),
    path('assy/profile/<int:pk>', ProfileUpdate.as_view(), name='profile'),
    #path('assy/profile/', views.photoupload, name='profile'),
    path('assy/delete/<int:pk>', PostDelete.as_view(), name='delete'),
]