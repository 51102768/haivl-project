from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Article(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="author")
    title = models.CharField(max_length=500)
    url = models.TextField()
    pub_date = models.DateField()

    def __unicode__(self):
        return self.title


class TypeArticle(models.Model):
    name = models.CharField(max_length=50)
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name="article")

    def __unicode__(self):
        return self.name