from django.db import models
from .category import Category

class Product(models.Model):
    name = models.CharField(max_length=30)
    price = models.IntegerField(default=100)
    
    # foreign key connection
    category = models.ForeignKey( Category, on_delete = models.CASCADE, default = 1)
    
    description = models.CharField(max_length=500)
    image = models.ImageField(upload_to='uploads/products/')
    

    #  all_entries = Entry.objects.all()
    @staticmethod
    def get_all_products():
        return Product.objects.all()
    
    
#     >>> Entry.objects.filter(
# ...     headline__startswith='What'
# ... ).exclude(
# ...     pub_date__gte=datetime.date.today()
# ... ).filter(
# ...     pub_date__gte=datetime.date(2005, 1, 30)
# ... )
    
    @staticmethod
    def get_all_products_by_categoryid(category_id):
        if category_id:
            return Product.objects.filter(category = category_id)
        else:
            return Product.get_all_products()
        


    # def getAllProducts():
    #     return Product.objects.all()
    
    
    
    #     skills = Skill.objects.filter(name__icontains=search_query)
    # profiles = Profile.objects.distinct().filter(
    #         Q(name__icontains=search_query) |
    #         Q(short_intro__icontains=search_query) |
    #         Q(skill__in=skills)
    #     )
