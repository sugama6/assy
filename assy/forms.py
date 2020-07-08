from allauth.account.forms import SignupForm
from django import forms
from .models import CustomUser, PostContents, RoomModel, Message
from allauth.account.adapter import DefaultAccountAdapter
from django.core.validators import MaxValueValidator, MinValueValidator


class CustomSignupForm(SignupForm):
    data = [
        ( 1, '男性'),
        ( 2 , '女性'),
    ]
    #email = forms.EmailField(label='hello')
    gender = forms.ChoiceField(choices=data) 
    age = forms.IntegerField(validators=[MinValueValidator(20),MaxValueValidator(99)])
    image = forms.ImageField()

    class Meta:
        model = CustomUser

    def signup(self, request,user):
        user.age = self.cleaned_data['age']
        user.gender = self.cleaned_data['gender']
        user.image = self.cleaned_data['image']
        user.save()
        return user
        
#投稿フォーム
class CreateForm(forms.ModelForm):
    class Meta:
        model = PostContents
        fields = ('place','date','member','contents')
        widgets = {
            'place': forms.TextInput(attrs={'placeholder':'例）○○駅'}),
            'date': forms.DateTimeInput(attrs={'placeholder': '例）yyyy-mm-dd hh:mm:ss'}),
            'contents': forms.TextInput(attrs={'placeholder':'例）終電なくしたので誰か迎えにきてください。'})
        }

#プロフィール編集フォーム
class ProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('username','email','age','gender','image')

#チャットフォーム
class RoomForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ('room','content','message_history')