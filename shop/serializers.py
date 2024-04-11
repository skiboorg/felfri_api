from rest_framework import exceptions, serializers, status, generics


from .models import *


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = '__all__'

class ProductTextBlockSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductTextBlock
        fields = '__all__'

class ProductComplectSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductComplect
        fields = '__all__'
class ProductFeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductFeature
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    complects = ProductComplectSerializer(many=True,required=False,read_only=True)
    features = ProductFeatureSerializer(many=True,required=False,read_only=True)
    images = ProductImageSerializer(many=True,required=False,read_only=True)
    text_blocks = ProductTextBlockSerializer(many=True,required=False,read_only=True)
    cat_slug = serializers.SerializerMethodField()
    cat_name = serializers.SerializerMethodField()
    subcat_slug = serializers.SerializerMethodField()
    subcat_name = serializers.SerializerMethodField()
    class Meta:
        model = Product
        fields = '__all__'
    def get_cat_slug(self,obj):
        return obj.subcategory.category.slug
    def get_cat_name(self,obj):
        return obj.subcategory.category.name
    def get_subcat_slug(self,obj):
        return obj.subcategory.slug

    def get_subcat_name(self,obj):
        return obj.subcategory.name

class ProductShortSerializer(serializers.ModelSerializer):
    cat_slug = serializers.SerializerMethodField()
    subcat_slug = serializers.SerializerMethodField()
    subcat_name = serializers.SerializerMethodField()
    subcat_text = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['name','slug','image_main','image_alt','price',
                  'cat_slug','subcat_name','file','subcat_slug','subcat_text',
                  'is_new',
                  'is_popular',
                  'is_active',
                  'is_arrive',
                  'is_in_stock'
                  ]
    def get_cat_slug(self,obj):
        return obj.subcategory.category.slug
    def get_subcat_slug(self,obj):
        return obj.subcategory.slug
    def get_subcat_name(self,obj):
        return obj.subcategory.name
    def get_subcat_text(self,obj):
        return obj.subcategory.short_description

class SubCategoryInstructuctionSerializer(serializers.ModelSerializer):
    products =serializers.SerializerMethodField()
    class Meta:
        model = SubCategory
        fields = ['products','name','image']

    def get_products(self, obj):
        products = []
        for product in obj.products.filter(is_active=True):
            if product.file:
                products.append(product)
        return ProductShortSerializer(products, many=True).data

class SubCategorySerializer(serializers.ModelSerializer):
    #products = ProductSerializer(many=True, required=False, read_only=True)
    products = serializers.SerializerMethodField()
    class Meta:
        model = SubCategory
        fields = '__all__'

    def get_products(self, obj):
        active_products = obj.products.filter(is_active=True)
        return ProductSerializer(active_products, many=True).data


class CategorySerializer(serializers.ModelSerializer):
    sub_categories = SubCategorySerializer(many=True, required=False, read_only=True)
    class Meta:
        model = Category
        fields = '__all__'


class SubCategoryShortSerializer(serializers.ModelSerializer):
    #products = ProductShortSerializer(many=True, required=False, read_only=True)
    products = serializers.SerializerMethodField()
    class Meta:
        model = SubCategory
        fields = '__all__'
    def get_products(self, obj):
        active_products = obj.products.filter(is_active=True)
        return ProductSerializer(active_products, many=True).data


class CategoryShortSerializer(serializers.ModelSerializer):
    sub_categories = SubCategoryShortSerializer(many=True, required=False, read_only=True)
    class Meta:
        model = Category
        fields = '__all__'






