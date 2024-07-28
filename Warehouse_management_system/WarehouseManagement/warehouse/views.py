from .models import Products
from .models import Customers
from .models import Suppliers
from .serializers import ProductsSerializer
from .serializers import CustomersSerializer
from .serializers import SuppliersSerializer
from rest_framework import viewsets


class ProductsViewSet(viewsets.ModelViewSet):

   serializer_class = ProductsSerializer
   queryset = Products.objects.all()


class CustomersViewSet(viewsets.ModelViewSet):

   serializer_class = CustomersSerializer
   queryset = Customers.objects.all()


class SuppliersViewSet(viewsets.ModelViewSet):

   serializer_class = SuppliersSerializer
   queryset = Suppliers.objects.all()


from .models import Order, Invoice
from .serializers import OrderSerializer, InvoiceSerializer



class OrderViewSet(viewsets.ModelViewSet):
   serializer_class = OrderSerializer
   queryset = Order.objects.all()


class InvoiceViewSet(viewsets.ModelViewSet):
   serializer_class = InvoiceSerializer
   queryset = Invoice.objects.all()

from .models import Report,Warehouse
from .serializers import ReportSerializer, WarehouseSerializer




class ReportViewSet(viewsets.ModelViewSet):
   queryset = Report.objects.all()
   serializer_class = ReportSerializer


class WarehouseViewSet(viewsets.ModelViewSet):
   queryset = Warehouse.objects.all()
   serializer_class = WarehouseSerializer