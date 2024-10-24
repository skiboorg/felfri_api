# Generated by Django 5.0.2 on 2024-10-24 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_newsitem_image_top'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsitem',
            name='page_description',
            field=models.TextField(blank=True, null=True, verbose_name='Description'),
        ),
        migrations.AddField(
            model_name='newsitem',
            name='page_title',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Title'),
        ),
    ]
