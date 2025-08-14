from django.contrib import admin
from .models import Category, Dish

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "order",)
    list_editable = ("order",)
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ("name",)

@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "price", "is_visible", "order")
    list_filter = ("category", "is_visible")
    list_editable = ("is_visible", "order")
    search_fields = ("name", "description")
