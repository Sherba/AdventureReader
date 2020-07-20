from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView
)
from .utils import get_story_depth
from .models import Genre, Node, Post


class PostListView(ListView):
    model = Post
    template_name = "stories/home.html"  
    # default: <app>/<model>_<viewtype>.html
    context_object_name = "posts"
    ordering = ["-date_posted"]
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        for post in context["posts"]:
            post.depth = get_story_depth(post.first_node)

        return context

class UserPostListView(ListView):
    model = Post
    template_name = "stories/user_posts.html"  
    context_object_name = "posts"
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get("username"))

        return Post.objects.filter(author=user).order_by("-date_posted")
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        for post in context["posts"]:
            post.depth = get_story_depth(post.first_node)

        return context

class PostDetailView(DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ["title", "content", "description", "genres"]
    # shares template with `update view`; <model>_form.html

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ["title", "content", "description", "genres"]

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
    success_url = "/"

    def test_func(self):
        post = self.get_object()

        if self.request.user == post.author:
            return True
        return False

class NodeDetailView(DetailView):
    model = Node

class NodeCreateView(LoginRequiredMixin, CreateView):
    model = Node
    fields = ["action", "content"]
    # shares template with `update view`; <model>_form.html

    def form_valid(self, form):
        form.instance.author = self.request.user

        parent = Node.objects.filter(pk=self.kwargs.get("pk")).first()

        form.save()
        form.instance.parent_node = parent
        form.instance.story = parent.story

        parent.child_nodes.add(form.instance)

        return super().form_valid(form)

class NodeUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Node
    fields = ["action", "content"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        node = self.get_object()

        if node.child_nodes.all():
            return False
        if self.request.user == node.author:
            return True
        return False

class NodeDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Node
    success_url = "/"

    def test_func(self):
        node = self.get_object()

        if node.child_nodes.all():
            return False
        if self.request.user == node.author:
            return True
        return False

class GenrePostListView(ListView):
    model = Post
    template_name = "stories/genre_posts.html"  
    context_object_name = "posts"
    paginate_by = 5

    def get_queryset(self):
        genre_name = self.kwargs.get("name")

        # USEFUL: m2m rel -> <m2m_field_name>__<field_to_lookup__contains>
        return Post.objects.filter(genres__name__contains=genre_name).order_by("-date_posted")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        for post in context["posts"]:
            post.depth = get_story_depth(post.first_node)

        return context

def about(request):
    return render(request, "stories/about.html", {"title": "About"})
