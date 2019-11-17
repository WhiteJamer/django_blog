from django.db import models
from postmanager.models import Post
from uprofile.models import User

class Comment(models.Model):
    body = models.TextField(max_length=700)
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE, blank=True, null=True)
    owner = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{0} - {1}'.format(self.pk, self.body)

