from django.urls import path
from rest_framework import routers
from .api import UserViewSet, PostViewSet, CommentViewSet, SubCommentViewSet, ImageViewSet, LogViewSet, DashboardAPIView

router = routers.SimpleRouter()
router.register(r'users', UserViewSet, basename="users")
router.register(r'posts', PostViewSet, basename="posts")
router.register(r'comments', CommentViewSet, basename="comments")
router.register(r'subcomments', SubCommentViewSet, basename="sub-comments")
router.register(r'images', ImageViewSet, basename="images")
router.register(r'logs', LogViewSet, basename="logs")

urlpatterns = [
    path('dashboard/', DashboardAPIView.as_view(), name="dashboard")
]+router.urls
