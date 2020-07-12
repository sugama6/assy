from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator
import uuid
# Create your models here.


GENDER_CHOICES = (
        (1, '男性'),
        (2, '女性'),
    )

class CustomUser(AbstractUser):

    class Meta(AbstractUser.Meta):
        db_table = 'auth_user'
        verbose_name_plural = 'CustomUser'

    age = models.IntegerField(blank=True, default=0,validators=[MinValueValidator(20),MaxValueValidator(99)])
    gender = models.IntegerField(choices=GENDER_CHOICES, blank=True, default=0)
    img = models.TextField(blank=True, default='icon_default.jpg')
    image = models.ImageField(upload_to='images/', verbose_name="画像", blank=True, null=True)

class PostContents(models.Model):
    post_id = models.AutoField(primary_key=True)
    #user_id = models.IntegerField(null=True)
    username = models.CharField(max_length=100, null=True)
    contents = models.TextField()
    member = models.IntegerField(null=True)
    reward = models.CharField(max_length=30)
    place = models.CharField(max_length=30)
    date = models.DateTimeField()
    post_time = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to='images/', verbose_name='画像', null=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.post_id)

class RoomModel(models.Model):
    room_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=100, null=True)
    chat_time = models.DateTimeField(default=timezone.now)
    #post = models.ForeignKey(PostContents, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.room_id)
 
class Message(models.Model):
    message_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    room = models.CharField(max_length=100, null=True)
    #room = models.ForeignKey(RoomModel, blank=True, null=True, related_name='room_messages', on_delete=models.CASCADE)
    content = models.TextField(null=True)
    message_history = models.TextField(null=True)
    created_at = models.DateTimeField(default=timezone.now, null=True)

    def __str__(self):
        return str(self.message_id)

