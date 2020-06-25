from django.urls import path
from .api import PostRequestAPIView, FeedbackAPIView

urlpatterns = [
    path('post-request/', PostRequestAPIView.as_view(), name="post-request"),
    path('feedback/', FeedbackAPIView.as_view(), name="feedback")
]
