from django import template

register = template.Library()


@register.filter(name='is_in_cart')
def is_in_cart(product,cart):
    keys = cart.keys()
    for id in keys:
        # print(id,product.id)
        # print(type(id),type(product.id))
        if int(id) == (product.id):
            return True
    return False
    
    
    # keys = cart.keys()
    # print(keys)
    # print(product,cart)
    # return True
    # {'1':'4','2':'3','4':'5'}
    # keys = cart.keys()
    # keys = {'1','2','3','4'}
    

# cart_quantity function

@register.filter(name='cart_quantity')
def cart_quantity(product,cart):
    keys = cart.keys()
    for id in keys:
        if int(id) == (product.id):
            return cart.get(id)
    return 0
 
 
 
 