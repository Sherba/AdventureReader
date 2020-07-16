from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Node, Post


@receiver(post_save, sender=Post)
def create_node(sender, instance, created, **kwargs):
    if created:
        # Node.objects.create(content="", action=None)
        n = Node(content="", action="Start Story", story=instance, author=instance.author)
        n.save()

        instance.first_node = n
        instance.save()
