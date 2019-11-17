from django.db import models
from django.urls import reverse_lazy
from pytils.translit import slugify

class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(blank=True)
    def __str__(self):
        return self.name
    # Создаем слаг из поля name и делаем транслит
    # если поле содержит киррилицу
    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)
    def get_absolute_url(self):
        return reverse_lazy('categorymanager:category_detail', kwargs={'slug':self.slug})
