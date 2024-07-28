from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from .models import Products
from .models import Customers
from .models import Suppliers


class ProductsSerializer(serializers.ModelSerializer):
   class Meta:
       model = Products
       fields = ['products_name', 'description', 'quantity', 'category', 'price']


class CustomersSerializer(serializers.ModelSerializer):
   class Meta:
       model = Customers
       fields = ['customer_name', 'phone', 'email', 'country', 'city', 'account_number']


class SuppliersSerializer(serializers.ModelSerializer):
   class Meta:
       model = Suppliers
       fields = ['suppliers_name', 'phone', 'email', 'country', 'city', 'account_number']


from .models import Order , Invoice


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['order_id', 'customer_name', 'order_date', 'financial_details', 'delivery_status']

class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = ['invoice_id', 'amount', 'payment_date', 'customer_or_supplier', 'invoice_date']


from .models import Report ,Warehouse


class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = ['report_id', 'stored_quantities', 'transfers', 'expenses', 'report_date']

class WarehouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Warehouse
        fields = ['name', 'address', 'space', 'storage_capacity']
