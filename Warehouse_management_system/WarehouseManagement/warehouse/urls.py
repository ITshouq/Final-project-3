from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('products', ProductsViewSet, basename='products')
router.register('customers', CustomersViewSet, basename='customers')
router.register('suppliers', SuppliersViewSet, basename='suppliers')

urlpatterns = [
  path('viewset/', include(router.urls)),
  path('viewset/<int:pk>/', include(router.urls)),

]

router.register('orders', OrderViewSet, basename='orders')
router.register('invoices', InvoiceViewSet, basename='invoices')

router.register('reports', InvoiceViewSet, basename='warehouses')

