from django.contrib import admin
from .models import Product, ProductImage, Collection


class ProductImageAdmin(admin.StackedInline):
    model = ProductImage

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageAdmin]
    class Meta:
        model = Product

@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    class Meta:
        model = Collection

@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    pass