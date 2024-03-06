from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=150, verbose_name='Заголовок')
    slug = models.CharField(max_length=150, verbose_name='slug')
    content = models.TextField(verbose_name='Содержимое')
    blog_image = models.ImageField(upload_to='products', verbose_name='Изображение', null=True, blank=True)
    created_at = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    publication = models.BooleanField(default=True, verbose_name='опубликовано')
    view_count = models.ImageField(default=0, verbose_name='просмотры')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'блог'
        verbose_name_plural = 'блоги'