from django.contrib import admin
from clothingStore.models import orderLine, Product, Customer

# Register your models here.
admin.site.register(orderLine)
admin.site.register(Product)
admin.site.register(Customer)

