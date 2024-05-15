from django.contrib import admin

from myapp.models import Client, Product, Order


# Register your models here.
class ClientAdmin(admin.ModelAdmin):
    """Список клиентов."""
    list_display = ['name', 'email', 'address']


class ProductAdmin(admin.ModelAdmin):
    """Список клиентов."""
    list_display = ['name', 'description', 'price']
    list_filter = ['added_date', 'price']


admin.site.register(Client, ClientAdmin)
admin.site.register(Product)
admin.site.register(Order)
