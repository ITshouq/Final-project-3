from django.contrib import admin
from .models import Products
from .models import Customers
from .models import Suppliers

# Register your models here.
admin.site.register(Products)
admin.site.register(Customers)
admin.site.register(Suppliers)

from .models import Order
from .models import Invoice


admin.site.register(Order)
admin.site.register(Invoice)

from .models import Report
from .models import Warehouse



admin.site.register(Report)
admin.site.register(Warehouse)

