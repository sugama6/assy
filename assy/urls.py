from django.urls import path, include
from . import views
from .views import HomeList, PostCreate, PostDelete, ProfileUpdate, chat
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('assy/home/', HomeList.as_view(), name='home'),
    path('assy/post/', PostCreate.as_view(), name='post'),
    path('assy/demo/', views.demo, name='demo'),
    path('assy/profile/<int:pk>', ProfileUpdate.as_view(), name='profile'),
    path('assy/delete/<int:pk>', PostDelete.as_view(), name='delete'),
    path('assy/chat/<str:username>/', views.chat, name='chat'),
 ] +  static(settings.IMAGE_URL, document_root=settings.IMAGE_ROOT)

