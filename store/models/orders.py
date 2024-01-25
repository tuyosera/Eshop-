from datetime import date
import datetime
from django.db import models
from .product import Product
from .customer import Customer
# from phone_field import PhoneField
# from phonenumber_field.phonenumber import PhoneNumber


class Orders(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField()
    address = models.CharField(max_length=50,default='')
    # phone =  models.IntegerField(null=True,default=1,blank=True)
    phone =  models.CharField(max_length=50,null=True,default=1,blank=True)
    date = models.DateField(default=datetime.datetime.today)
    
    
    def autoCheckValues(self,product,customer,quantity,price,address,phone):
    
        try:
            if product or customer or quantity or price or address or phone is not None:
                return True   
        except (TypeError, ValueError) as e:
            # field_name = self.name
            # if self.verbose_name:
            #     field_name = self.verbose_name
            raise e.__class__("Custom Error Message") from e
            
        
    
    
    
    def placeOrder(self):
        self.save(using='default')

    
# Demo refrence class
# class CustomIntegerField(models.Field):
#     def get_prep_value(self, value):
#         value = super().get_prep_value(value)
#         if value is None:
#             return None
#         try:
#             return int(value)
#         except (TypeError, ValueError) as e:
#             field_name = self.name
#             if self.verbose_name:
#                 field_name = self.verbose_name
#             raise e.__class__("Custom Error Message") from e

# class CustomAutoField(AutoFieldMixin, CustomIntegerField, metaclass=AutoFieldMeta):