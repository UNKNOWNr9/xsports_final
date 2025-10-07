from rest_framework import serializers

from blog_module.models import Article, ArticleComment


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'