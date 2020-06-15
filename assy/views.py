from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import PostContents, ChatModel, CustomUser
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from .forms import CreateForm, ProfileForm
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.contrib import messages
from django.http import HttpResponse


class HomeList(ListView):
    print("--HomeList(ListView): --")
    template_name = 'assy/home.html'
    model = PostContents
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'more_context': PostContents.objects.order_by('-post_time')
        })
        return context

def chat(request):
    return render(request, 'assy/chat.html')

class PostCreate(CreateView):
    template_name = 'assy/post.html'
    model = PostContents
    form_class = CreateForm
    success_url = reverse_lazy('home')
    
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user_id = self.request.user.id
        self.object.username = self.request.username
        self.object.image = self.request.user.image
        self.object.save()

        messages.success(self.request, "保存しました")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.warning(self.request, form.errors)
        return super().form_invalid(form)

def update(request, id):
    obj = CustomUser.objects.get(id=id)
    if request.method == 'POST':
        obj.image = request.FILES['image']
        user = ProfileForm(request.POST, instance=obj)
        user.save()
        
        return redirect(to='/assy/home')
    params = {
        'id': id,
        'form': ProfileForm(instance=obj),
        'context': obj
    }
    return render(request, 'assy/profile.html', params)

   
#投稿削除
class PostDelete(DeleteView):
    model = PostContents
    success_url = reverse_lazy('home')