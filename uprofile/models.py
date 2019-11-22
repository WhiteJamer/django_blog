from django.db import models
from django.urls import reverse_lazy
from django.contrib.auth.models import AbstractUser
from time import time
from pytils.translit import slugify

class User(AbstractUser):
    slug = models.SlugField(max_length=255, unique=True)
    rating = models.IntegerField(default=0, blank=True, null=True)
    avatar = models.FileField(upload_to='avatars/', default='no-image-user.png')
    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = self.username
        super(User, self).save(*args, **kwargs)
    def get_absolute_url(self):
        return reverse_lazy('uprofile:user_detail', kwargs={'slug': self.slug})

