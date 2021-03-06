from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Node(models.Model):
    content = models.TextField()
    action = models.CharField(max_length=100, null=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    child_nodes = models.ManyToManyField("self", symmetrical=False, related_name="children")
    parent_node = models.ForeignKey("self", on_delete=models.CASCADE, related_name="parents", null=True)
    story = models.ForeignKey("Post", on_delete=models.CASCADE, null=True)

    def __str__(self):
        # return f"Story Node after action: '{self.action}', by author: {self.author}"
        return f"Story: {self.story} - Action: {self.action}"

    def get_absolute_url(self):
        """Function will be called if `success_url` is not given."""
        return reverse("node-detail", kwargs={"pk": self.parent_node.pk if self.parent_node else self.id})

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    description = models.TextField(default="")
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    first_node = models.ForeignKey(Node, on_delete=models.SET_NULL, null=True)
    genres = models.ManyToManyField("Genre", blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """Function will be called if `success_url` is not given."""
        return reverse("post-detail", kwargs={"pk": self.pk})

class Genre(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name
