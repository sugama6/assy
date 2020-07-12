from django.contrib import admin

# Register your models here.
from .models import PostContents, CustomUser, RoomModel, Message

admin.site.register(PostContents)
admin.site.register(CustomUser)
admin.site.register(RoomModel)
admin.site.register(Message)
