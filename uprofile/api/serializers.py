from rest_framework import serializers
from uprofile.models import User


class OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'slug', 'avatar']