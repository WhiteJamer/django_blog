from django.db import models
from django.urls import reverse_lazy
from pytils.translit import slugify

class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(blank=True, unique=True)
    def __str__(self):
        return self.name
    # Создаем слаг из поля name и делаем транслит
    # если поле содержит киррилицу
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)
    def get_absolute_url(self):
        return reverse_lazy('postmanager:post_list') + '?category={0}'.format(self.slug)
