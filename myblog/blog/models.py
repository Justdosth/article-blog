# blog/models.py
from django.db import models

class Comment(models.Model):
    article = models.ForeignKey('Article', on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return self.text

class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    topic = models.CharField(max_length=100)
    comments = models.ManyToManyField(Comment, related_name='article_comments', blank=True)

    def __str__(self):
        return self.title
