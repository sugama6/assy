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

def message(request):
    room_list = RoomModel.objects.order_by('-chat_time')[:5]
    template = loader.get_template('assy/message.html')
    context = {
        'room_list': room_list,
    }
    return HttpResponse(template.render(context, request))

#チャット画面
#def chat(request, room_name):
#    messages = Message.objects.filter(room__name=room_name).order_by('-chat_time')[:50]
#    room = RoomModel.objects.filter(name=room_name)[0]
#    template = loader.get_template('assy/room.html')
#    context = {
#        'messages': messages,
#        'room': room
#    }
#    return HttpResponse(template.render(context, request))
#class RoomView(ListView):
#    template_name = 'assy/room.html'
#    model = Message
#
#    def get_context_data(self, **kwargs):
#        context = super().get_context_data(**kwargs)
#        context.update({
#            'username': self.request.user.username,
#            'form': RoomForm,
#        })
#        return context
#
#    def form_valid(self, form):
#        self.object = form.save(commit=False)
#        self.object.name = self.request.user.username
#        self.object.save()
 
def room(request, username):
    user1 = CustomUser.objects.filter(username=username)
    print(user1)
    
    if request.method == 'POST':
        #content = request.POST['content']
        #message_history = request.POST['message_history']
        #message = Message(content=content, message_history=message_history)
        message = RoomForm(request.POST, instance=user1)
        message.save()
    params = {
        'form': RoomForm(),
        'username': username,
        'user1': user1
        }
    return render(request, 'assy/chat.html', params)  
##def room(request):s
#    return render(request, 'assy/room.html')

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

    def form_valid(self, form):
        self.object = form.save(commit=False)
        return super().form_valid(form)
   
#投稿削除
class PostDelete(DeleteView):
    model = PostContents
    success_url = reverse_lazy('home')

def demo(request):
    return render(request, 'assy/demo.html')