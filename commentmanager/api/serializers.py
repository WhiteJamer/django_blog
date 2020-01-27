from rest_framework import serializers
from commentmanager.models import Comment
from uprofile.api.serializers import OwnerSerializer

class PostCommentsSerializer(serializers.ModelSerializer):
    owner = OwnerSerializer()
    class Meta:
        model = Comment
        fields = ['body', 'post', 'owner', 'created_at']