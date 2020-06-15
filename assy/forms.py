from allauth.account.forms import SignupForm
from django import forms
from .models import CustomUser, PostContents
from allauth.account.adapter import DefaultAccountAdapter


class CustomSignupForm(SignupForm):
    data = [
        ( 1, '男性'),
        ( 2 , '女性'),
    ]
    gender = forms.ChoiceField(choices=data, widget=forms.RadioSelect()) 
    age = forms.IntegerField()
    image = forms.ImageField()

    class Meta:
        model = CustomUser

    def signup(self, request,user):
        user.age = self.cleaned_data['age']
        user.gender = self.cleaned_data['gender']
        user.image = self.cleaned_data['image']
        user.save()
        return user

class ProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('username','email','age','gender','image')


#未完成
class CreateForm(forms.ModelForm):
    class Meta:
        model = PostContents
        fields = ('place','date','member','contents')
        widgets = {
            'place': forms.TextInput(attrs={'placeholder':'例）○○駅'}),
            'date': forms.DateTimeInput(attrs={'placeholder': '例）yyyy-mm-dd hh:mm:ss'}),
            'contents': forms.TextInput(attrs={'placeholder':'例）終電なくしたので誰か迎えにきてください。'})
        }

#class PostCreateForm(forms.Form):
#    class Meta:
#        model = PostContents
#        image = forms.ImageField()
#        email = forms.EmailField()