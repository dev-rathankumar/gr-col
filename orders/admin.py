from django.contrib import admin
from .models import Payment, Order, OrderProduct

# Register your models here.

class OrderProductInLine(admin.TabularInline):
    model = OrderProduct
    readonly_fields = ('payment', 'user', 'product')
    extra = 0

class OrderAdmin(admin.ModelAdmin):
    list_display = ['order_number', 'full_name','phone', 'email','city', 'state', 'zip_code','order_total','tax', 'status', 'is_ordered']
    list_filter = ['status', 'is_ordered']
    search_fields = ['order_number', 'first_name','last_name', 'phone', 'email']
    list_per_page = 20
    inLines = [OrderProductInLine]


admin.site.register(Order, OrderAdmin)
admin.site.register(Payment)
admin.site.register(OrderProduct)
