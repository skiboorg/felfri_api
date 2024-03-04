# Generated by Django 5.0.2 on 2024-03-01 09:52

import django_resized.forms
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_num', models.IntegerField(default=10)),
                ('image_big', django_resized.forms.ResizedImageField(crop=None, force_format='WEBP', keep_meta=True, null=True, quality=95, scale=None, size=[1440, 640], upload_to='banner/images', verbose_name='Баннер десктоп')),
                ('image_small', django_resized.forms.ResizedImageField(crop=None, force_format='WEBP', keep_meta=True, null=True, quality=95, scale=None, size=[760, 640], upload_to='banner/images', verbose_name='Баннер мобилка')),
                ('text_big', models.TextField(blank=True, null=True, verbose_name='Текст большой')),
                ('text_small', models.TextField(blank=True, null=True, verbose_name='Текст маленький')),
            ],
            options={
                'verbose_name': 'Баннер',
                'verbose_name_plural': 'Баннеры',
                'ordering': ['order_num'],
            },
        ),
    ]