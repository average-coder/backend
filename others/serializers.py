from rest_framework import serializers
from .models import PostRequest, Feedback


class PostRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostRequest
        fields = "__all__"


class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = "__all__"
