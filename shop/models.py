from django.db import models
from pytils.translit import slugify
from django_ckeditor_5.fields import CKEditor5Field
from django_resized import ResizedImageField

class Category(models.Model):
    order_num = models.IntegerField(default=1, null=True)
    image = ResizedImageField(size=[420, 420], quality=95, force_format='WEBP', upload_to='shop/category/images',
                              blank=True, null=True)
    name = models.CharField('Название', max_length=255, blank=False, null=False)
    name_alt = models.CharField('Название1', max_length=255, blank=True, null=False)
    slug = models.CharField('ЧПУ', max_length=255,
                            help_text='Если не заполнено, создается на основе поля Назавание',
                            blank=True, null=True, editable=False)
    show_at_equipment = models.BooleanField('Вывод в меню', default=True, null=False)

    def __str__(self):
        return f'{self.name}'

    def save(self, *args, **kwargs):

        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    class Meta:
        ordering = ('order_num',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class SubCategory(models.Model):
    order_num = models.IntegerField(default=1, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=False, null=True, related_name='sub_categories')
    name = models.CharField('Название', max_length=255, blank=False, null=False)
    slug = models.CharField('ЧПУ', max_length=255,
                            help_text='Если не заполнено, создается на основе поля Назавание',
                            blank=True, null=True, editable=False)
    image = ResizedImageField(size=[420, 420], quality=95, force_format='WEBP', upload_to='shop/category/images',
                              blank=False, null=True)
    short_description = models.TextField('Короткое описание', blank=True, null=False)
    html_content = CKEditor5Field('SEO текст', blank=True, null=False)
    is_active= models.BooleanField('Отображать', default=True, null=False)

    def __str__(self):
        return f'{self.name}'

    def save(self, *args, **kwargs):

        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    class Meta:
        ordering = ('order_num',)
        verbose_name = 'Подкатегория'
        verbose_name_plural = 'Подкатегории'

class Product(models.Model):
    order_num = models.IntegerField(default=1, null=True)
    subcategory = models.ForeignKey(SubCategory,blank=True,null=True,on_delete=models.CASCADE, related_name='products')
    is_new = models.BooleanField('Новинка', default=False, null=False)
    is_popular = models.BooleanField('Популярный', default=False, null=False)
    is_active = models.BooleanField('Отображать?', default=True, null=False)
    is_arrive = models.BooleanField('В пути?', default=False, null=False)
    is_in_stock = models.BooleanField('В наличии?', default=True, null=False)
    image_main = ResizedImageField(size=[800, 600], quality=95, force_format='WEBP', upload_to='shop/product/images',
                              blank=False, null=True)
    image_alt = ResizedImageField(size=[800, 600], quality=95, force_format='WEBP', upload_to='shop/product/images',
                                   blank=False, null=True)
    name = models.CharField('Название', max_length=255, blank=False, null=True)
    slug = models.CharField('ЧПУ',max_length=255,
                            help_text='Если не заполнено, создается на основе поля Назавание',
                            blank=True, null=True, editable=False)
    price = models.CharField('Цена', max_length=255, blank=True, null=True)
    description = models.TextField('Описание', blank=True, null=True)
    html_content = CKEditor5Field('SEO текст', blank=True, null=False, config_name='extends', editable=False)
    wb_link = models.CharField('Ссылка Wb', max_length=255, blank=True, null=True)
    ozon_link = models.CharField('Ссылка Ozon', max_length=255, blank=True, null=True)
    file = models.FileField('Файл инструкции', upload_to='shop/product/files', blank=True, null=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        ordering = ('order_num',)
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def save(self, *args, **kwargs):

        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=False,
                                related_name='images')
    image = ResizedImageField(size=[800, 600], quality=95, force_format='WEBP', upload_to='shop/product/images',
                              blank=False, null=True)
    def __str__(self):
        return f''
    class Meta:

        verbose_name = 'Доп. изображение товара'
        verbose_name_plural = 'Доп. изображения товара'


class ProductFeature(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=False,
                                related_name='features')
    label = models.CharField('Название', max_length=255, blank=False, null=True)
    value = models.CharField('Значение', max_length=255, blank=False, null=True)

    def __str__(self):
        return f'{self.label}'

    class Meta:
        verbose_name = 'Характеристика'
        verbose_name_plural = 'Характеристики'


class ProductComplect(models.Model):
    order_num = models.IntegerField(default=1, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=False,
                                related_name='complects')
    label = models.CharField('Название', max_length=255, blank=False, null=True)
    value = models.CharField('Значение', max_length=255, blank=False, null=True)
    image = ResizedImageField(size=[100, 100], quality=95, force_format='WEBP', upload_to='shop/product/images',
                              blank=False, null=True)
    def __str__(self):
        return f'{self.label}'

    class Meta:
        ordering = ('order_num',)
        verbose_name = 'Комплектация'
        verbose_name_plural = 'Комплектации'


class ProductTextBlock(models.Model):
    order_num = models.IntegerField(default=1, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=False,
                                related_name='text_blocks')
    html_content = CKEditor5Field('текст', blank=True, null=False, config_name='extends')

    image = ResizedImageField(size=[700, 560], quality=95, force_format='WEBP', upload_to='shop/product/images',
                              blank=False, null=True)
    is_image_right = models.BooleanField('Картинка справа',default=False, null=False)
    def __str__(self):
        return f'{self.order_num}'

    class Meta:
        ordering = ('order_num',)
        verbose_name = 'Текстовый блок'
        verbose_name_plural = 'Текстовые блоки'