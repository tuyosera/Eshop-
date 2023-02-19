from datetime import date
from django.db import models

class Customer(models.Model):
    
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    # models.IntegerField(default=100)
    email = models.CharField(max_length=50,default='name@gmail.com')
    password = models.CharField(max_length=500)
 
    
    # for saving the SIgn up Customers data
    def register(self):
        self.save()
        
        
    # Checking that the Email is already registered or not
    # >>> Entry.objects.filter 
    def emailExists(self):
        if Customer.objects.filter(email = self.email):
            return True
        else:
            return False
       
        
    # getting the customer object by email     
    def get_customer_by_email(email):
        # for getting the QUERY SET 
        # return Customer.objects.filter(email = email)
        
        # for gettin a single customer object
        return Customer.objects.get(email = email)
        

        

        
    
