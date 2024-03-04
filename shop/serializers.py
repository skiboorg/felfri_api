from rest_framework import exceptions, serializers, status, generics


from .models import *


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
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
    cat_slug = serializers.SerializerMethodField()
    cat_name = serializers.SerializerMethodField()
    class Meta:
        model = Product
        fields = '__all__'
    def get_cat_slug(self,obj):
        return obj.subcategory.category.slug
    def get_cat_name(self,obj):
        return obj.subcategory.category.name

class ProductShortSerializer(serializers.ModelSerializer):
    cat_slug = serializers.SerializerMethodField()
    subcat_name = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['name','slug','image_main','image_alt','price','cat_slug','subcat_name']
    def get_cat_slug(self,obj):
        return obj.subcategory.category.slug
    def get_subcat_name(self,obj):
        return obj.subcategory.name

class SubCategorySerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, required=False, read_only=True)
    class Meta:
        model = SubCategory
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    sub_categories = SubCategorySerializer(many=True, required=False, read_only=True)
    class Meta:
        model = Category
        fields = '__all__'


class SubCategoryShortSerializer(serializers.ModelSerializer):
    products = ProductShortSerializer(many=True, required=False, read_only=True)
    class Meta:
        model = SubCategory
        fields = '__all__'


class CategoryShortSerializer(serializers.ModelSerializer):
    sub_categories = SubCategoryShortSerializer(many=True, required=False, read_only=True)
    class Meta:
        model = Category
        fields = '__all__'






