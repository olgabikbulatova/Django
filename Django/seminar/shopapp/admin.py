from django.contrib import admin
from .models import Product, Order, Client


# Register your models here.


@admin.action(description="Сбросить количество в ноль")
def reset_quantity(modeladmin, request, queryset):
    queryset.update(quantity=0)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'quantity', 'image']
    ordering = ['price', '-quantity']
    list_filter = ['add_day', 'price']
    search_fields = ['description']
    search_help_text = 'Поиск по полю Описание продукта(description)'
    actions = [reset_quantity]
    """Отдельный продукт."""
    # fields = ['name', 'description', 'quantity', 'add_day', 'price', 'image']
    readonly_fields = ['add_day', 'image']
    fieldsets = [
        (None,
         {
             'classes': ['wide'],
             'fields': ['name'],
         },
         ),
        (
            'Подробности',
            {
                'classes': ['collapse'],
                'description': 'Категория товара и его подробное описание',
                'fields': ['image', 'description'],
            },
        ),
        (
            'Бухгалтерия',
            {
                'fields': ['price', 'quantity'],
            }
        ),
        (
            'Рейтинг и прочее',
            {
                'description': 'Рейтинг сформирован автоматически на основе оценок покупателей',
                'fields': ['add_day'],
            }
        ),
    ]


class ClientAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'reg_day']
    ordering = ['name', '-reg_day']
    list_filter = ['name', 'phone']
    search_fields = ['name']
    search_help_text = 'Поиск по полю Имя клиента(name)'
    actions = [reset_quantity]
    """Отдельный продукт."""
    readonly_fields = ['reg_day']
    fieldsets = [
        (None,
         {
             'classes': ['wide'],
             'fields': ['name'],
         },
         ),
        (
            'Подробности',
            {
                'classes': ['collapse'],
                'description': 'Подробная инфорамция о клиенте',
                'fields': ['reg_day'],
            },
        ),
        (
            'Контактные данные',
            {
                'fields': ['phone', 'email', 'address'],
            }
        )
    ]


# @admin.action(description="Discount 100%")
def discount_total(modeladmin, request, queryset):
    queryset.update(total_price=00.00)


class OrderAdmin(admin.ModelAdmin):
    list_display = ['customer', 'date_ordered', 'total_price']
    ordering = ['customer', '-date_ordered']
    list_filter = ['customer', 'total_price']
    search_fields = ['customer']
    search_help_text = 'Поиск по полю Имя клиента(customer)'
    actions = [discount_total]
    """Отдельный продукт."""
    readonly_fields = ['date_ordered']
    fieldsets = [
        (None,
         {
             'classes': ['wide'],
             'fields': ['customer'],
         },
         ),
        (
            'Товары',
            {
                'classes': ['collapse'],
                'description': 'список продуктов в заказе',
                'fields': ['products'],
            },
        ),
        (
            'Прочие данные заказа',
            {
                'fields': ['date_ordered', 'total_price'],
            }
        )
    ]


admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Client, ClientAdmin)
