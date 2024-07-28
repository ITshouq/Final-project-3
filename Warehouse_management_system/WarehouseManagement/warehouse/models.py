from django.db import models


class Products(models.Model):
   products_name = models.CharField(max_length=100)
   description = models.TextField(max_length=255)
   quantity = models.IntegerField(null=True)
   category = models.CharField(max_length=100)
   price = models.FloatField(null=True)

   def str(self):
       return self.products_name


class Customers(models.Model):
   customer_name = models.CharField(max_length=100)
   phone = models.IntegerField(null=True)
   email = models.EmailField(null=True)
   country = models.CharField(max_length=100)
   city = models.CharField(max_length=100)
   account_number = models.PositiveBigIntegerField(null=True)

   def str(self):
       return self.customer_name


class Suppliers(models.Model):
   suppliers_name = models.CharField(max_length=100)
   phone2 = models.IntegerField(null=True)
   email2 = models.EmailField(null=True)
   country2 = models.CharField(max_length=100)
   city2 = models.CharField(max_length=100)
   account_number2 = models.PositiveBigIntegerField(null=True)

   def str(self):
       return self.suppliers_name



class Order(models.Model):
    order_id = models.CharField(max_length=100, unique=True)
    customer_name = models.CharField(max_length=100)
    order_date = models.DateTimeField(auto_now_add=True)
    financial_details = models.TextField()
    delivery_status = models.CharField(max_length=50)

    def str(self):
        return self.order_id


class Invoice(models.Model):
    invoice_id = models.CharField(max_length=100, unique=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateTimeField()
    customer_or_supplier = models.CharField(max_length=100)
    invoice_date = models.DateTimeField(auto_now_add=True)

    def str(self):
        return self.invoice_id

class Report(models.Model):
 report_id = models.CharField(max_length=100, unique=True)
 stored_quantities = models.DecimalField(max_digits=10, decimal_places=2)
 transfers = models.PositiveIntegerField()
 expenses = models.DecimalField(max_digits=10, decimal_places=2)
 report_date = models.DateTimeField(auto_now_add=True)

 def __str__(self):
   return self.report_id


class Warehouse(models.Model):
 name = models.CharField(max_length=100)
 address = models.CharField(max_length=255)
 space = models.DecimalField(max_digits=10, decimal_places=2)
 storage_capacity = models.DecimalField(max_digits=10, decimal_places=2)

 def __str__(self):
   return self.name