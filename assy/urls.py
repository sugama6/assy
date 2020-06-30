from django.urls import path, include
from . import views
from .views import HomeList, PostCreate, chat, PostDelete, ProfileUpdate
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('assy/home/', HomeList.as_view(), name='home'),
    path('assy/post/', PostCreate.as_view(), name='post'),
    path('assy/chat/', views.chat, name='chat'),
    #path('assy/profile/<int:id>', views.update, name='profile'),
    path('assy/profile/<int:pk>', ProfileUpdate.as_view(), name='profile'),
    path('assy/delete/<int:pk>', PostDelete.as_view(), name='delete'),
] +  static(settings.IMAGE_URL, document_root=settings.IMAGE_ROOT)
#if settings.DEBUG:
#    urlpatterns += static(settings.IMAGE_URL, document_root=settings.IMAGE_ROOT)
