from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=32, verbose_name='название категории')

    class Meta:
        verbose_nane = 'Категория'
        verbose_name_plural = 'Категории'
    
    def __str__(self):
        return self.name