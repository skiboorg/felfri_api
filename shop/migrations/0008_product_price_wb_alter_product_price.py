# Generated by Django 5.0.2 on 2024-06-21 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_product_article_num'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='price_wb',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Цена WB'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Цена Ozon'),
        ),
    ]
