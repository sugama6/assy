from django.urls import path, include
from . import views
from .views import HomeList, PostCreate, PostDelete, ProfileUpdate, room, message
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('assy/home/', HomeList.as_view(), name='home'),
    path('assy/post/', PostCreate.as_view(), name='post'),
    path('assy/demo/', views.demo, name='demo'),
    path('assy/profile/<int:pk>', ProfileUpdate.as_view(), name='profile'),
    path('assy/delete/<int:pk>', PostDelete.as_view(), name='delete'),
    path('assy/message/', views.message, name='message'),
    path('assy/room/<str:username>/', views.room, name='room'),
    #path('assy/<str:username>/', views.room, name='room'),
    #path('assy/room/', views.room, name='room')
 ] +  static(settings.IMAGE_URL, document_root=settings.IMAGE_ROOT)
#if settings.DEBUG:
#    urlpatterns += static(settings.IMAGE_URL, document_root=settings.IMAGE_ROOT)
