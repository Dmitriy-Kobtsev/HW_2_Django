# Generated by Django 4.2.10 on 2024-03-30 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0007_alter_product_options_product_is_published'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='is_published',
            field=models.BooleanField(default=True),
        ),
    ]
