from .serializers import UserSerializer, PostSerializer, CommentSerializer, SubCommentSerializer, ImageSerializer, LogSerializer
from rest_framework import viewsets, generics, filters
from django.contrib.auth.models import User
from posts.models import Post, Comment, SubComment, Image
from rest_framework.permissions import IsAdminUser
from rest_framework_tracking.models import APIRequestLog
from rest_framework.response import Response
from django.utils import timezone
from django.utils.timezone import timedelta
from rest_framework import pagination

class TestPagination(pagination.PageNumberPagination):       
    page_size = 10


class UserViewSet(viewsets.ModelViewSet):
    pagination_class=TestPagination
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['username']
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [ IsAdminUser, ]


class PostViewSet(viewsets.ModelViewSet):
    pagination_class=TestPagination
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title']
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    permission_classes = [ IsAdminUser, ]


class CommentViewSet(viewsets.ModelViewSet):
    pagination_class=TestPagination
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['id']
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    permission_classes = [ IsAdminUser, ]


class SubCommentViewSet(viewsets.ModelViewSet):
    pagination_class=TestPagination
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['id']
    serializer_class = SubCommentSerializer
    queryset = SubComment.objects.all()
    permission_classes = [ IsAdminUser, ]


class ImageViewSet(viewsets.ModelViewSet):
    pagination_class=TestPagination
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['id']
    serializer_class = ImageSerializer
    queryset = Image.objects.all()
    permission_classes = [ IsAdminUser, ]


class LogViewSet(viewsets.ReadOnlyModelViewSet):
    pagination_class=TestPagination
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['id', 'path', 'errors', 'status_code']
    serializer_class = LogSerializer 
    queryset = APIRequestLog.objects.all()
    permission_classes = [ IsAdminUser, ]


class DashboardAPIView(generics.GenericAPIView):
    pagination_class=TestPagination
    permission_classes = [ IsAdminUser, ]

    def get(self, request):

        count_all_time_total = APIRequestLog.objects.all().count()
        count_today_total = APIRequestLog.objects.filter(requested_at__date=timezone.now().date()).count()
        count_week_total = APIRequestLog.objects.filter(requested_at__gte=timezone.now()-timedelta(days=7)).count()

        count_all_time_unique = APIRequestLog.objects.values('remote_addr').distinct().count()
        count_today_unique = APIRequestLog.objects.filter(requested_at__date=timezone.now().date()).values('remote_addr').distinct().count()
        count_week_unique = APIRequestLog.objects.filter(requested_at__gte=timezone.now()-timedelta(days=7)).values('remote_addr').distinct().count()

        posts_count = Post.objects.all().count()
        comment_count = Comment.objects.all().count() + SubComment.objects.all().count()
       
        editor_count = User.objects.all().count()
        image_count = Image.objects.all().count()

        return Response({
            "count_today_total": count_today_total,
            "count_today_unique": count_today_unique,
            "count_week_total": count_week_total,
            "count_week_unique": count_week_unique,
            "count_all_time_total":count_all_time_total,
            "count_all_time_unique": count_all_time_unique,
            "posts_count": posts_count,
            "comment_count": comment_count,
            "editor_count": editor_count,
            "image_count": image_count
        })
