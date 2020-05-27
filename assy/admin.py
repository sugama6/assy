from django.contrib import admin

# Register your models here.
from .models import PostContents, ChatModel

admin.site.register(PostContents)
admin.site.register(ChatModel)