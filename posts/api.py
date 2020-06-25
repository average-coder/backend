from .serializers import PostSerializer, ImageSerializer, CommentSerializer, SubCommentSerializer, PostListSerializer, EditorPostSerializer, CreateCommentSerializer, CreateSubCommentSerializer
from rest_framework import generics, filters, viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated
from .models import Post, Image


class PostListAPI(generics.ListAPIView):
    search_fields = ['title']
    filter_backends = (filters.SearchFilter,)
    serializer_class = PostListSerializer
    permission_classes = [ AllowAny, ]
    queryset = Post.objects.all().order_by('-date_posted')


class PostAPI(viewsets.ReadOnlyModelViewSet):
    serializer_class = PostSerializer
    permission_classes = [ AllowAny, ]
    lookup_field = 'slug'
    queryset = Post.objects.all().order_by('-date_posted')


class EditorListAPI(generics.ListAPIView):
    serializer_class = PostListSerializer
    permission_classes = [ IsAuthenticated, ]
    search_fields = ['title']
    filter_backends = (filters.SearchFilter,)

    def get_queryset(self):
        return self.request.user.posts


class EditorAPI(viewsets.ModelViewSet):
    serializer_class = EditorPostSerializer
    permission_classes = [ IsAuthenticated, ]
    
    def get_queryset(self):
        return self.request.user.posts
    
    def perform_create(self, serializer):
        serializer.save(author = self.request.user)


class ImageAPI(viewsets.ModelViewSet):
    serializer_class = ImageSerializer
    permission_classes = [ IsAuthenticated, ]
    queryset = Image.objects.all()


class CommentAPI(generics.CreateAPIView):
    serializer_class = CreateCommentSerializer
    permission_classes = [ AllowAny, ]


class SubCommentAPI(generics.CreateAPIView):
    serializer_class = CreateSubCommentSerializer
    permission_classes = [ AllowAny, ]


class SuggestionsAPI(generics.ListAPIView):
    serializer_class = PostListSerializer
    permission_classes = [ AllowAny, ]
    queryset = Post.objects.all().order_by('-date_posted')[:3]