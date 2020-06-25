from rest_framework import serializers
from .models import Post, Image, Comment, SubComment


class SubCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubComment
        fields = "__all__"


class CommentSerializer(serializers.ModelSerializer):
    sub_comments = SubCommentSerializer(many = True)
    class Meta:
        model = Comment
        fields = "__all__"


class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many = True)
    username = serializers.CharField(source='author.username', read_only=True)
    class Meta:
        model = Post
        fields = "__all__"


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = "__all__"


class PostListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ["id", "title", "slug", "date_posted"]


class EditorPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"


class CreateCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"


class CreateSubCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubComment
        fields = "__all__"