from django.contrib.auth import get_user_model
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
    owner = models.ForeignKey(get_user_model(),
                              on_delete=models.SET_NULL,
                              verbose_name='Владелец',
                              null=True,
                              blank=True
                              )
    is_published = models.BooleanField(default=False)

    def __str__(self):
        # Строковое отображение объекта
        return f'{self.product_name} {self.product_price} {self.product_category}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'

        permissions = [
            (
                'set_published',
                'Can publish product'
            )
        ]


class Version(models.Model):
    product = models.ForeignKey(Product, verbose_name='Версия', on_delete=models.SET_NULL, null=True, blank=True)
    version_number = models.FloatField(verbose_name='Номер версии')
    version_name = models.CharField(max_length=150, verbose_name='Название версии')
    version_current = models.BooleanField(verbose_name='Признак текущей версии', default=False)

    def __str__(self):
        return f'версия {self.version_name} {self.version_number}'

    class Meta:
        verbose_name = 'Версия'
        verbose_name_plural = 'Версии'