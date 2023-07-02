from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=32, verbose_name='название категории')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
    
    def __str__(self):
        return self.name
    
    
class Tovar(models.Model):
    name = models.CharField(max_length=96, verbose_name='название товара')
    image = models.ImageField(upload_to='%y/%m/%d', verbose_name='изображение')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='категория')
    text = models.CharField(max_length=500, verbose_name='описане') 
    price = models.CharField(max_length=5, verbose_name='цена')
    count = models.IntegerField()

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.name