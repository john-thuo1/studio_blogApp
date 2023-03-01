from django.urls import path
from . import views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView

# Note : 
'''
you have to call as_view() function for class based views so as to return a callable view that takes a request and returns a response.
Its the main entry-point in request-response cycle in case of generic views. as_view is the function(class method) which will connect my MyView class with its url.
'''
urlpatterns = [
    # path("", views.home, name='blog-home'),
    path("", PostListView.as_view(), name='blog-home'),
    path("user/<str:username>", UserPostListView.as_view(), name='user-posts'),

    path('post/<int:pk>', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),


    path('about/', views.about, name='blog-about'),
]
