from django.contrib import admin
from .models import OrderUpdate, Product, Contact, Orders

# Register your models here.
admin.site.register(Product)
admin.site.register(Contact)
admin.site.register(Orders)
admin.site.register(OrderUpdate)