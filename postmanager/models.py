from django.db import models
from uprofile.models import User
from categorymanager.models import Category
from django.urls import reverse_lazy
from django.urls import reverse
from pytils.translit import slugify # для перевода киррилицы в латиницу

class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    slug = models.SlugField(blank=True)
    owner = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    categories = models.ManyToManyField(Category, related_name='posts')
    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)
        super(Post, self).save(*args, *kwargs)
    def get_absolute_url(self):
        return reverse('postmanager:post_detail', kwargs={'slug': self.slug})
