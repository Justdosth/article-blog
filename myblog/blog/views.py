# blog/views.py
from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics
from .models import Article, Comment
from .serializers import ArticleSerializer, CommentSerializer
from .forms import CommentForm

class ArticleListAPIView(generics.ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def list(self, request, *args, **kwargs):
        articles = self.get_queryset()
        return render(request, 'blog/article_list.html', {'articles': articles})

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        return render(request, self.template_name, {'article': instance})

class CommentListAPIView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        article_id = self.request.query_params.get('article_id')
        article = get_object_or_404(Article, pk=article_id)
        serializer.save(article=article)

class CommentDetailAPIView(generics.RetrieveAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class ArticleDetailAPIView(generics.RetrieveAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        form = CommentForm()
        return render(request, 'blog/article_details.html', {'article': serializer.data, 'form': form})

class CommentListForArticleView(generics.ListAPIView):
    serializer_class = CommentSerializer

    def get_queryset(self):
        article_id = self.request.query_params.get('article_id')
        article = get_object_or_404(Article, pk=article_id)
        return article.comments.all()

@api_view(['GET'])
def get_article_list(request):
    articles = Article.objects.all()
    serializer = ArticleSerializer(articles, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_article_details(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    serializer = ArticleSerializer(article)
    return Response(serializer.data)

@api_view(['GET'])
def filter_by_topic(request, topic):
    articles = Article.objects.filter(topic=topic)
    serializer = ArticleSerializer(articles, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def submit_comment(request):
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['GET'])
def get_article_api(request):
    articles = Article.objects.all()
    serializer = ArticleSerializer(articles, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
