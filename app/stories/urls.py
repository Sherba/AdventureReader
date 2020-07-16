from django.urls import path
from .views import (
    NodeCreateView,
    NodeDetailView,
    PostCreateView, 
    PostDetailView, 
    PostListView, 
    PostUpdateView, 
    PostDeleteView,
    UserPostListView,
)
from . import views

urlpatterns = [
    path("", PostListView.as_view(), name="stories-home"),
    path("user/<str:username>", UserPostListView.as_view(), name="user-posts"),
    path("post/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path("post/new/", PostCreateView.as_view(), name="post-create"),
    path("post/<int:pk>/update/", PostUpdateView.as_view(), name="post-update"),
    path("post/<int:pk>/delete/", PostDeleteView.as_view(), name="post-delete"),
    path("about/", views.about, name="stories-about"),
    path("node/<int:pk>/", NodeDetailView.as_view(), name="node-detail"),
    path("node/<int:pk>/new", NodeCreateView.as_view(), name="node-create"),
]
