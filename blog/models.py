from django.db import models
from django.contrib.auth.models import User
import uuid
from django.urls import reverse

# Create your models here.


class Post(models.Model):
    uuid = models.UUIDField(auto_created=True, unique=True, default=uuid.uuid4)
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE)  # relacionamento
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'slug': self.slug})
