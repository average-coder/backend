from django.contrib.auth.models import User
from posts.models import Post, Comment, SubComment, Image
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email", "first_name", "last_name"]


class PostSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='author.username', read_only=True)
    class Meta:
        model = Post
        fields = ["id", "title", "slug", "date_posted", "username", "data"]


class SubCommentSerializer(serializers.ModelSerializer):
    post = serializers.CharField(source='comment.post.id', read_only=True)
    class Meta:
        model = SubComment
        fields = "__all__"


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = "__all__"