# blog/urls.py
from django.urls import path
from .views import get_article_list, get_article_details, filter_by_topic, submit_comment, get_article_api
from .views import ArticleListAPIView, ArticleDetailAPIView, CommentListAPIView, CommentDetailAPIView, CommentListForArticleView

urlpatterns = [
    # path('comments/', CommentListForArticleView.as_view(), name='get_comment_list_for_article'),
    path('articles/', ArticleListAPIView.as_view(), name='get_article_list'),
    path('articles/<int:pk>/', ArticleDetailAPIView.as_view(), name='get_article_details'),
    path('articles/topic/<str:topic>/', filter_by_topic),
    path('comments/', CommentListAPIView.as_view(), name='get_comment_list'),
    path('comments/<int:pk>/', CommentDetailAPIView.as_view(), name='get_comment_details'),
    path('comments/add/', CommentListAPIView.as_view(), name='add_comment'),
]
