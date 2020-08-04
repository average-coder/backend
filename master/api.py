from .serializers import UserSerializer, PostSerializer, CommentSerializer, SubCommentSerializer, ImageSerializer
from rest_framework import viewsets, filters
from django.contrib.auth.models import User
from posts.models import Post, Comment, SubComment, Image
from rest_framework.permissions import IsAdminUser


class UserViewSet(viewsets.ModelViewSet):
    search_fields = ['username']
    filter_backends = (filters.SearchFilter,)
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [ IsAdminUser, ]


class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    permission_classes = [ IsAdminUser, ]


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    permission_classes = [ IsAdminUser, ]


class SubCommentViewSet(viewsets.ModelViewSet):
    serializer_class = SubCommentSerializer
    queryset = SubComment.objects.all()
    permission_classes = [ IsAdminUser, ]


class ImageViewSet(viewsets.ModelViewSet):
    serializer_class = ImageSerializer
    queryset = Image.objects.all()
    permission_classes = [ IsAdminUser, ]