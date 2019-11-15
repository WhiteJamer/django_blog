from django.db import models
from pytils.translit import slugify

class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(blank=True)

    # Создаем слаг из поля name и делаем транслит
    # если поле содержит киррилицу
    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)