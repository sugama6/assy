from django.contrib import admin

# Register your models here.
from .models import PostContents, CustomUser, RoomModel

admin.site.register(PostContents)
admin.site.register(CustomUser)
admin.site.register(RoomModel)
