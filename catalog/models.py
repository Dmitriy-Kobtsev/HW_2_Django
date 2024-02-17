from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name='Наименование')
    about = models.TextField(verbose_name='Описание')

    def __str__(self):
        # Строковое отображение объекта
        return f'{self.name}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Product(models.Model):
    product_name = models.CharField(max_length=150, verbose_name='Название')
    product_about = models.TextField(verbose_name='Описание')
    image = models.ImageField(upload_to='products', verbose_name='Изображение', null=True, blank=True)
    product_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    product_price = models.IntegerField(verbose_name='Цена')
    created_at = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Дата последнего изменения', auto_now=True)

    def __str__(self):
        # Строковое отображение объекта
        return f'{self.product_name} {self.product_price} {self.product_category}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'