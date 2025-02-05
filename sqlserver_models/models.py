from django.db import models

class NED(models.Model):
    is_ned_model = True
    
    class Meta:
        abstract = True
        managed = False

class EnterpriseInfo2(NED):
    EnterpriseID = models.CharField(primary_key=True, max_length=255)
    LCICID = models.CharField(max_length=255)
    enterpriseNameLao = models.CharField(max_length=255, null=True)
    
    class Meta(NED.Meta):
        db_table = 'EnterpriseInfo2'
class Soneserver2(NED):
    EnterpriseID = models.CharField(primary_key=True, max_length=255)
    LCICID = models.CharField(max_length=255)
    enterpriseNameLao = models.CharField(max_length=255, null=True)
    
    class Meta(NED.Meta):
        db_table = 'Soneserver2'
class Soneserver1(NED):
    EnterpriseID = models.CharField(primary_key=True, max_length=255)
    LCICID = models.CharField(max_length=255)
    enterpriseNameLao = models.CharField(max_length=255, null=True)
    
    class Meta(NED.Meta):
        db_table = 'Soneserver1'

# Simple Customer model
# class Customer(models.Model):
#     name = models.CharField(max_length=100)
#     email = models.EmailField(unique=True)

#     def __str__(self):
#         return self.name

# # Simple Order model
# class Order(models.Model):
#     customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
#     order_date = models.DateTimeField(auto_now_add=True)
#     total_amount = models.DecimalField(max_digits=10, decimal_places=2)

#     def __str__(self):
#         return f"Order {self.id} for {self.customer.name}"
    
# class Employee_LCIC(models.Model):
#     name = models.CharField(max_length=100)
#     surname = models.CharField(max_length=100)

#     def __str__(self):
#         return self.name