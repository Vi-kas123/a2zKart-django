from django.contrib import admin
from .models import Products,Variation,ReviewRating
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name','price','stock','category','modified_date','is_available')
    prepopulated_fields = {'slug':('product_name',)}
 

class VariationAdmin(admin.ModelAdmin):
    list_display = ('product','variation_category','is_active')
    list_editable = ('is_active',)
    list_filter = ('product','variation_category')
    

admin.site.register(Products,ProductAdmin)
admin.site.register(Variation,VariationAdmin)
admin.site.register(ReviewRating)
