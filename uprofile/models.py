from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    slug = models.SlugField(max_length=255)
    def save(self, *args, **kwargs): #Слаг по умолчанию
        if not self.id:
            self.slug = self.username
        super(User, self).save(*args, **kwargs)
    def get_absolute_url(self):
        return self.slug

