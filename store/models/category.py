from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=20)
    
    @staticmethod
    def get_all_category():
        return Category.objects.all()
    
    # Print the name of Category
    def __str__(self):
        return self.name

    # >>> all_entries = Entry.objects.all()
    


