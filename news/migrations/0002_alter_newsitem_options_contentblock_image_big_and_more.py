# Generated by Django 5.0.2 on 2024-02-28 18:40

import django_resized.forms
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='newsitem',
            options={'ordering': ('order_num',), 'verbose_name': 'Новость', 'verbose_name_plural': 'Новости'},
        ),
        migrations.AddField(
            model_name='contentblock',
            name='image_big',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, force_format='WEBP', keep_meta=True, null=True, quality=95, scale=None, size=[1440, 500], upload_to='news/images', verbose_name='Одиночная картинка'),
        ),
        migrations.AlterField(
            model_name='contentblock',
            name='image',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, force_format='WEBP', keep_meta=True, null=True, quality=95, scale=None, size=[520, 400], upload_to='news/images', verbose_name='Картинка с текстом'),
        ),
        migrations.AlterField(
            model_name='contentblocktype',
            name='slug',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='ЧПУ'),
        ),
    ]
