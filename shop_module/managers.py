from django.db import models


class ProductManager(models.Manager):
    def published(self):
        return self.filter(is_active=True)
