from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import PostContents, CustomUser, RoomModel, Message
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from .forms import CreateForm, ProfileForm, RoomForm
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.contrib import messages
from django.http import HttpResponse
from django.template import loader

#ホーム画面
class HomeList(ListView):
    template_name = 'assy/home.html'
    model = CustomUser
        
    def get_context_data(self, **kwargs):
        sql = PostContents.objects.select_related('user').order_by('-post_time')
        context = super().get_context_data(**kwargs)
        context.update({
            'more_context': sql
        })
        return context

def message(request, name):
    post = PostContents.objects.filter(username=name)
    room = RoomModel(name=name,request_id=request.user.id)
    room.save()
    params = {
        'form': RoomForm(),    #フォーム
        'username': name,    #ユーザー名
        'post': post,
        'chat_list': RoomModel.objects.filter(request_id=request.user.id).order_by('chat_time'),
        'users': CustomUser.objects.all(),
        'message': Message.objects.filter(room=name)
        }
    if request.method == 'POST':
        content = request.POST['content']
        message_history = Message(message_history=content, room=name)
        message_history.save()
    return render(request, 'assy/message.html', params)  

#チャット画面
def chat(request, username):
    post = PostContents.objects.filter(username=username)
    room = RoomModel(name=username,request_id=request.user.id)
    #room.save()
    params = {
        'form': RoomForm(),    #フォーム
        'username': username,    #ユーザー名
        'post': post,
        'chat_list': RoomModel.objects.filter(request_id=request.user.id).order_by('chat_time'),
        'users': CustomUser.objects.all(),
        'message': Message.objects.filter(room=username),
        #'repuest_message': Message.objects.filter(request_user=request.user.username),
        }
    if request.method == 'POST':
        content = request.POST['content']
        message_history = Message(message_history=content, room=username, request_user=request.user.username)
        message_history.save()
    return render(request, 'assy/chat.html', params)  

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
class ProfileUpdate(UpdateView):
    template_name = 'assy/profile.html'
    model = CustomUser
    fields = ('username','age','email','gender','image')
    success_url = reverse_lazy('home')

    #def form_valid(self, form):
    #    self.object = form.save(commit=False)
    #    return super().form_valid(form)
   
#投稿削除
class PostDelete(DeleteView):
    model = PostContents
    success_url = reverse_lazy('home')

def demo(request):
    return render(request, 'assy/demo.html')