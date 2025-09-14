from django.db import models

class ArticleManager(models.Manager):
    def published(self):
        return self.filter(status='PB')