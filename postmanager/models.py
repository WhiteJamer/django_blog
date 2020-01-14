from django.db import models
from uprofile.models import User
from categorymanager.models import Category
from django.urls import reverse_lazy
from django.urls import reverse
from pytils.translit import slugify  # для перевода киррилицы в латиницу
from tinymce.models import HTMLField
from time import time


class Post(models.Model):
    title = models.CharField(max_length=255)
    content = HTMLField()
    slug = models.SlugField(blank=True)
    owner = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    categories = models.ManyToManyField(Category, related_name='posts', blank=True, null=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.id and not self.slug:
            self.slug = str(int(time())) + '_' + slugify(self.title)
        elif not self.id and self.slug:
            self.slug = slugify(self.slug)
        super(Post, self).save(*args, *kwargs)

    def get_absolute_url(self):
        return reverse('postmanager:post_detail', kwargs={'slug': self.slug})
