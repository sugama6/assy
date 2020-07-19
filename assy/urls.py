from django.urls import path, include
from . import views
from .views import HomeList, PostCreate, PostDelete, ProfileUpdate, chat, message
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('assy/home/', HomeList.as_view(), name='home'),
    path('assy/post/', PostCreate.as_view(), name='post'),
    path('assy/demo/', views.demo, name='demo'),
    path('assy/profile/<int:pk>', ProfileUpdate.as_view(), name='profile'),
    path('assy/delete/<int:pk>', PostDelete.as_view(), name='delete'),
    #path('assy/room/<int:id>/', views.room, name='room'),
    path('assy/chat/<str:username>/', views.chat, name='chat'),
    path('assy/message/<str:name>', views.message, name='message'),
 ] +  static(settings.IMAGE_URL, document_root=settings.IMAGE_ROOT)

