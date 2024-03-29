# Generated by Django 4.2.10 on 2024-03-06 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Заголовок')),
                ('slug', models.CharField(max_length=150, verbose_name='slug')),
                ('content', models.TextField(verbose_name='Содержимое')),
                ('blog_image', models.ImageField(blank=True, null=True, upload_to='products', verbose_name='Изображение')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('publication', models.BooleanField(default=True, verbose_name='опубликовано')),
                ('view_count', models.ImageField(default=0, upload_to='', verbose_name='просмотры')),
            ],
            options={
                'verbose_name': 'блог',
                'verbose_name_plural': 'блоги',
            },
        ),
    ]
