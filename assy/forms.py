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

    class Meta:
        model = CustomUser

    def signup(self, request,user):
        #user.image = self.cleaned_data['image']
        user.age = self.cleaned_data['age']
        user.gender = self.cleaned_data['gender']
        user.save()
        return user

#class PostCreateForm(forms.ModelForm):
#    class Meta:
#        model = PostContents
#        fields = '__all__'
#        widgets = {
#            'place': forms.TextInput(attrs={'placeholder':'例）○○駅'}),
#        }

class PostCreateForm(forms.Form):
    class Meta:
        model = PostContents
        image = forms.ImageField()