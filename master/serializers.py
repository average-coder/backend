from django.contrib.auth.models import User
from posts.models import Post, Comment, SubComment, Image
from rest_framework import serializers
from rest_framework_tracking.models import APIRequestLog


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email", "first_name", "last_name", "is_superuser", "password"]
        extra_kwargs = { 'password': {'write_only': True}}

        def create(self, validate_data):
            user = User.objects.create_user(
                validate_data['username'],
                validate_data['email'],
                validate_data['password'],
                validate_data['first_name'],
                validate_data['last_name'],
                validate_data['is_superuser'],
            )
            return user


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


class LogSerializer(serializers.ModelSerializer):
    class Meta:
        model = APIRequestLog
        fields = ['id', 'requested_at', 'response_ms', 'path', 'remote_addr',
                  'host', 'method', 'query_params', 'errors', 'status_code']
