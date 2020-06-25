from django.urls import path
from .api import PostListAPI, PostAPI, EditorListAPI, EditorAPI, ImageAPI, CommentAPI, SubCommentAPI, SuggestionsAPI
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'editor', EditorAPI, basename="editor-api")
router.register(r'post', PostAPI, basename="post-api")
router.register(r'image', ImageAPI, basename="image-api")

urlpatterns = [
    path('list/', PostListAPI.as_view(), name='list-posts'),
    path('editor-list/', EditorListAPI.as_view(), name='editor-list'),
    path('comment/', CommentAPI.as_view(), name='comment-api'),
    path('sub-comment/', SubCommentAPI.as_view(), name='sub-comment-api'),
    path('suggestions/', SuggestionsAPI.as_view(), name='suggestion')
]

urlpatterns += router.urls

