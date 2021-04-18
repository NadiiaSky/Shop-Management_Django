from django.contrib import admin
from .models import Shop, Product, Category


# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    fields = ['product_title', 'description', 'amount', 'price', 'images', 'active']
    search_fields = ['title']


class ShopAdmin(admin.ModelAdmin):
    search_fields = ['title']


admin.site.register(Shop, ShopAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
