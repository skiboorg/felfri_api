from django.contrib import admin
from nested_inline.admin import NestedStackedInline, NestedModelAdmin
from django.utils.safestring import mark_safe
from .models import *
class ProductTextBlockInline(NestedStackedInline):
    model = ProductTextBlock
    extra = 0

class ProductFeatureInline(NestedStackedInline):
    model = ProductFeature
    extra = 0

class ProductComplectInline(NestedStackedInline):
    model = ProductComplect
    extra = 0

class ProductImageInline(NestedStackedInline):
    model = ProductImage
    extra = 0

class ProductAdmin(NestedModelAdmin):
    model = Product
    inlines = [ProductTextBlockInline,ProductFeatureInline,ProductImageInline,ProductComplectInline]
    readonly_fields = ['image_preview']

    def image_preview(self, obj):

        if obj.image_main:
            return mark_safe(
                '<img src="{0}" width="150" height="150" style="object-fit:contain" />'.format(obj.image_main.url))
        else:
            return 'Нет изображения'

    image_preview.short_description = 'Текущее изображение'




admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Product, ProductAdmin)
