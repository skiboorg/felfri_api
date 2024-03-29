# Generated by Django 5.0.2 on 2024-03-07 07:34

import django.db.models.deletion
import django_ckeditor_5.fields
import django_resized.forms
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_category_name_alt'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductTextBlock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_num', models.IntegerField(default=1, null=True)),
                ('html_content', django_ckeditor_5.fields.CKEditor5Field(blank=True, verbose_name='текст')),
                ('image', django_resized.forms.ResizedImageField(crop=None, force_format='WEBP', keep_meta=True, null=True, quality=95, scale=None, size=[700, 560], upload_to='shop/product/images')),
                ('is_image_right', models.BooleanField(default=False, verbose_name='Картинка справа')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='text_blocks', to='shop.product')),
            ],
            options={
                'verbose_name': 'Текстовый блок',
                'verbose_name_plural': 'Текстовые блоки',
                'ordering': ('order_num',),
            },
        ),
    ]
