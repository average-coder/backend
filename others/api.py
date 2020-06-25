from .serializers import PostRequestSerializer, FeedbackSerializer
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated


class PostRequestAPIView(generics.CreateAPIView):
    serializer_class = PostRequestSerializer
    permission_classes = [ AllowAny, ]


class FeedbackAPIView(generics.CreateAPIView):
    serializer_class = FeedbackSerializer
    permission_classes = [ AllowAny, ]