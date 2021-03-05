from django.contrib import admin

# Register your models here.

from .models import Item, Articles, Category, Cart, CartItem, Order, OrderItem


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    pass


@admin.register(Articles)
class ArticlesAdmin(admin.ModelAdmin):
    pass

class OrderItemTabularInline(admin.TabularInline):
    model = OrderItem

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderItemTabularInline]
    list_filter = ('date',)
    ordering = ['-date']
    list_display = ('get_user', 'get_quantity', 'get_date', )
    pass


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


class CartAdmin(admin.ModelAdmin):
    pass


class CartItemAdmin(admin.ModelAdmin):
    pass


class CartItemTabularInline(admin.TabularInline):
    model = CartItem


class UserCartAdmin(admin.ModelAdmin):
    inlines = [CartItemTabularInline]
    list_filter = ('status_checked', )

    class Meta:
        model = Cart


admin.site.register(Cart, UserCartAdmin)
