from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import PostContents, ChatModel, CustomUser
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from .forms import CreateForm, ProfileForm
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.contrib import messages
from django.http import HttpResponse
from django.db.models import F

#ホーム画面
class HomeList(ListView):
    template_name = 'assy/home.html'
    model = CustomUser
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'more_context': PostContents.objects.order_by('-post_time')
        })
        return context

def chat(request):
    return render(request, 'assy/chat.html')

#新規投稿
class PostCreate(CreateView):
    template_name = 'assy/post.html'
    model = PostContents
    form_class = CreateForm
    success_url = reverse_lazy('home')
    
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user_id = self.request.user.id
        self.object.image = self.request.user.image
        self.object.username = self.request.user.username
        self.object.save()

        messages.success(self.request, "保存しました")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.warning(self.request, form.errors)
        return super().form_invalid(form)

#プロフィール編集
#def update(request, id):
#    obj = CustomUser.objects.get(id=id)
#    post = PostContents.objects.filter(user_id=id).values('user_id','username','image')
#    if request.method == 'POST':
#        form = ProfileForm(request.POST, request.FILES, instance=obj)
#        form.save()
#       
#        #post['image'] = request.user.image
#        #post['username'] = request.user.username
#        #post.save()
#        return redirect(to='/assy/home')
#    params = {
#        'id': id,
#        'form': ProfileForm(instance=obj),
#    }
#    return render(request, 'assy/profile.html', params)
class ProfileUpdate(UpdateView):
    template_name = 'assy/profile.html'
    model = CustomUser
    fields = ('username','age','email','gender','image')
    success_url = reverse_lazy('home')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = PostContents.objects.filter(user_id=id).values('user_id')
        print(post)
        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        return super().form_valid(form)
   
#投稿削除
class PostDelete(DeleteView):
    model = PostContents
    success_url = reverse_lazy('home')