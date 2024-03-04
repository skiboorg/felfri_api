from django.urls import path,include
from . import views

urlpatterns = [
    path('categories', views.GetCategories.as_view()),
    path('instructions', views.GetInstructions.as_view()),
    path('categories/<slug>', views.GetCategory.as_view()),
    path('subcategory/<slug>', views.GetSubCategory.as_view()),
    path('product/<slug>', views.GetProduct.as_view()),
    path('new', views.GetNewProducts.as_view()),
    path('popular', views.GetPopularProducts.as_view()),
]
