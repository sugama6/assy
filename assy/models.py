from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
# Create your models here.


GENDER_CHOICES = (
        (1, '男性'),
        (2, '女性'),
    )

class CustomUser(AbstractUser):

    class Meta(AbstractUser.Meta):
        db_table = 'auth_user'
        verbose_name_plural = 'CustomUser'

    age = models.IntegerField(blank=True, default=0)
    gender = models.IntegerField(choices=GENDER_CHOICES, blank=True, default=0)
    img = models.TextField(blank=True, default='icon_default.jpg')
    image = models.ImageField(upload_to='images/', verbose_name="画像", null=True)

class PostContents(models.Model):
    post_id = models.AutoField(primary_key=True)
    user_id = models.IntegerField(null=True)
    contents = models.TextField()
    member = models.IntegerField(null=True)
    reward = models.CharField(max_length=30)
    place = models.CharField(max_length=30)
    date = models.DateTimeField()
    post_time = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to='images/', verbose_name='画像', null=True)

    def __str__(self):
        return str(self.post_id)

class ChatModel(models.Model):
    chat_id = models.AutoField(primary_key=True, default=0)
    user_id = models.IntegerField()
    chat_time = models.DateTimeField(auto_now=True)
    response_nm = models.CharField(max_length=30)
    response_id = models.CharField(max_length=30)
    chat_history = models.TextField()

    def __str__(self):
        return str(self.chat_id)


