from django.contrib import admin
from .models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'first_name', 'last_name', 'email', 'address', 'city', 'postal_code', 'paid', 'created', 'updated']
    list_filter = ['paid', 'updated', 'created']
    inlines = [OrderItemInline]
