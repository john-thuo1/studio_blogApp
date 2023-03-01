from django.shortcuts import render, get_object_or_404
from .models import Post
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView,CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
# Create your views here.


def home(request):
    context = {
        'posts': Post.objects.all(),
    }

    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html')

# 
#-------------------------------------------------------------------------------------------------------------------
# Posts Views
# Post List View
class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    # We want posts to be shown in the order of recently created to oldest
    ordering = ['-date_created']
    paginate_by = 5

# User Posts List Views
class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'
    context_object_name = 'posts'
    # We want posts to be shown in the order of recently created to oldest
    ordering = ['-date_created']
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs['username'])
        return Post.objects.filter(author=user).order_by('-date_created')

# Class Post Details View

class PostDetailView(DetailView):
    model = Post
   
# Post Create View 
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']
    
    # Override the form_validation method to take in current user logged in as the author of the post he/she submits
    def form_valid(self, form):
        # Before submitting the post, take the current user logged in as the author of the post
        form.instance.author = self.request.user
        return super().form_valid(form)
    

# Post Update View
class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Post
    fields = ['title', 'content']
    
    # Override the form_validation method to take in current user logged in as the author of the post he/she submits
    def form_valid(self, form):
        # Before submitting the post, take the current user logged in as the author of the post
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        # Check to see that the user updating a given post is the author of the post
        if self.request.user == post.author:
            return True
        return False
    

# Post Delete View


class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin, DeleteView):
    model = Post 
    # Once you delete a post, you are redirected to the home page
    success_url= '/'
    def test_func(self):
        post = self.get_object()
        # Check to see that the user updating a given post is the author of the post
        if self.request.user == post.author:
            return True
        return False
    