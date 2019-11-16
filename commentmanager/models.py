from django.db import models
from postmanager.models import Post
from uprofile.models import User

class Comment(models.Model):
    body = models.TextField(max_length=700)
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    owner = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

