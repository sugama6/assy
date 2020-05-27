from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import PostContents, ChatModel, CustomUser
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from .forms import PostCreateForm
from django.contrib.auth.decorators import login_required
from django.views import generic


class HomeList(ListView):
    print("--HomeList(ListView): --")
    template_name = 'assy/home.html'
    model = PostContents

    def get(self, request, *args, **kwargs):
        self.object = None
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = None
        self.object_list = self.get_queryset()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'more_context': PostContents.objects.all
        })
        post_list = CustomUser.objects.all().order_by('pk')[:]
        return context
    def get_queryset(self):
        return CustomUser.objects.order_by('pk')

def chat(request):
    return render(request, 'assy/chat.html', {'some': 100})

class PostCreate(CreateView):
    template_name = 'assy/post.html'
    model = PostContents
    fields = ('place','date','member','contents')
    success_url = reverse_lazy('home')

#def create(request):
#    params = {
#        'form': PostCreateForm(),
#    }
#    if (request.method == 'POST'):
#        place = request.POST['place']
#        member = int(request.POST['member'])
#        date_0 = request.POST['date_0']
#        date_1 = request.POST['date_1']
#        contents = request.POST['contents']
#        post = PostContents(place=place, member=member, date=date_0 + date_1, contents=contents)
#        post.save()
#        return redirect(to='assy/home')
#    return render(request, 'assy/post.html', params)
    

class ProfileUpdate(UpdateView):
    template_name = 'assy/profile.html'
    model = CustomUser
    fields = ('username','email','age','gender')
    success_url = reverse_lazy('home')
   

#def photoupload(request):
#    if request.method == 'GET':
#        
#      return render(request, 'assy/profile.html', {
#        'form': PostCreateForm(),
#   })
#    elif request.method == 'POST':
#        form = PostCreateForm(request.POST, request.FILES)
#        if not form.is_valid():
#           raise ValueError('invalid form')
#        photo = CustomUser()
#        photo.image = form.cleaned_data['image']
#        photo.save()
#        return redirect('home')
#
#
#投稿削除
class PostDelete(DeleteView):
    model = PostContents
    success_url = reverse_lazy('home')