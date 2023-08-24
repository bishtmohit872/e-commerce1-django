from django.contrib import admin
from .models import product,contact,orders,orderupdate,signup

# Register your models here.

admin.site.register(product)
admin.site.register(contact)
admin.site.register(orders)
admin.site.register(orderupdate)
admin.site.register(signup)
