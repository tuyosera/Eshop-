from django.contrib import admin
from .models.product import Product
from .models.category import Category
from .models.contact import Contact
from .models.customer import Customer


# Display the name of the PRODUCTS
class AdminProducts(admin.ModelAdmin):
    list_display = ['name','price','category']


# Display the name of the CATEGORY
class AdminCategory(admin.ModelAdmin):
    list_display = ['name']


# Register your models here.
# products
admin.site.register(Product,AdminProducts)
admin.site.register(Category,AdminCategory)
admin.site.register(Contact)
admin.site.register(Customer)



# AdminProducts
