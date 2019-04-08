from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from friendship.models import Friend, Follow
from .models import Post, Item
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'hubble/home.html', context)

class PostListView(ListView):
    model = Post
    template_name = 'hubble/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 4
    
    
class UserPostListView(ListView):
    model = Post
    template_name = 'hubble/user_posts.html'
    context_object_name = 'posts'
    paginate_by = 4
    
    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')
    
    
class PostDetailView(DetailView):
    model = Post
 
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'subtitle', 'content']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'subtitle', 'content']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
    
class HubPostListView(ListView):
    model = Post
    template_name = 'hubble/hub.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 4

class MarketListView(ListView):
    model = Item
    template_name = 'hubble/market.html'
    context_object_name = 'items'
    ordering = ['-date_posted']
    paginate_by = 4
    
class ItemDetailView(DetailView):
    model = Item
    
class ItemCreateView(LoginRequiredMixin, CreateView):
    model = Item
    fields = ['title', 'price', 'image']
    
    def form_valid(self, form):
        form.instance.seller = self.request.user
        return super().form_valid(form)
    
class ItemUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Item
    fields = ['title', 'price', 'image']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        item = self.get_object()
        if self.request.user == item.seller:
            return True
        return False
    
class ItemDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Item
    success_url = '/'
    
    def test_func(self):
        item = self.get_object()
        if self.request.user == item.seller:
            return True
        return False
    
class ItemPurchaseView(DeleteView):
    model = Item
    success_url = '/'
    
def market(request):
    context = {
        'items': Item.objects.all()
    }
    return render(request, 'hubble/market.html', context)

def hull (request):
    return render(request, 'hubble/hull.html',
    {'title': 'University of Hull'})

# Create your views here.
