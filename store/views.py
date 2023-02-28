
from django.shortcuts import render
from store import templates
from django.views import View
from django.contrib.auth.hashers import make_password,check_password

from store.models.product import Product
from store.models.category import Category

from django.shortcuts import render , redirect , HttpResponseRedirect
from store.models.product import Product
from store.models.category import Category
from django.views import View


from django.shortcuts import render
from store import templates
from django.views import View


from store.models.contact import Contact


from store.models.customer import Customer


# Encode and Decode 
# https://base64.guru/converter/decode
# "cart":{"2":4,"5":1,"6":1,"9":2,"3":1}


# Create your views here.

# class Index(View):    
#     def get(self,request):
#         return render(request,'store/index.html')
    
#     def post(self,request):
#         # return HttpResponse('Hi this is INDEX method ')
#         #empty dict.
#         data = {}
#         # products = Product.get_all_products()
#         categories = Category.get_all_category()

#         # print(products)
#         # print(categories)
        
#         # Getting the products by category_ID
#         categoryID = request.GET.get('category')
        
#         if categoryID:
#             products = Product.get_all_products_by_categoryid(categoryID)
#             print(products)
#         else:
#             products = Product.get_all_products()
#             print(products)
            
#         data['products'] = products
#         data['categories'] = categories
#         request.sessions['products'] = True
#         return render(request,'index.html',data)

def index(request):
    ## GET request
    if request.method == 'GET':
        
        # Clearing the Session
        # this will clear/ refresh all the data in the session
        # request.session.clear()
        # request.session.flush()
        # return HttpResponse('Hi this is INDEX method ')
        #empty dict.
        data = {}
        
        # Initializing the CART
        cart = request.session.get('cart')
        # MEthod 1 
        if not cart:
            cart = {}
        
        # Method 2 :
        # if cart:
        #     pass
        # else:
        #     cart = {}
               
        
        

        # if I have to clear the cart object in the session 
        # request.session.get('cart').clear()
        
        
        # products = Product.get_all_products()
        categories = Category.get_all_category()

        # print(products)
        # print(categories)
        
        # Getting the products by category_ID
        categoryID = request.GET.get('category')
        
        if categoryID:
            products = Product.get_all_products_by_categoryid(categoryID)
        else:
            products = Product.get_all_products()
            
        data['products'] = products
        data['categories'] = categories
        
        # catch the SESSION data that we added in LOGIN class
        print('you are logged in as : ',request.session.get('email'))
        
        return render(request,'store/index.html',data)

    # POST reqeust
    else:
        # to get the product id from add to cart button
        product_id = request.POST.get('product_id')
        # print(product_id)
        cart = request.session.get('cart')
        
        # if we get any REMOVE product request then cath it here
        remove = request.POST.get('remove')
        
        # if cart already exists 
        if cart:
            quantity = cart.get(product_id)
            if quantity:
                # if we get a REMOVE product request
                if remove:
                    # if the questity is 1 then delete the product from the CART
                    if quantity == 1:
                        # Delete the product from the ID
                        cart.pop(product_id)
                    else:    
                        cart[product_id] = quantity - 1    
                else:
                    cart[product_id] = quantity + 1
            else:
                cart[product_id] = 1
        else:
            cart = {}
            cart[product_id] = 1
        request.session['cart'] = cart
        print('your cart ',request.session['cart'])
               
        return redirect('/')




#Signup
class Signup(View):
    
    def get(self,request):
        return render(request,'signup.html')
    
    def post(self,request):
        return Signup.if_Post_request(request)

    # to handle POST request in SIGNUP            
    def if_Post_request(request):
            # if request.method == 'POST':
            postData = request.POST
            firstname = postData.get('firstname')
            lastname = postData.get('lastname')
            email = postData.get('email')
            password = postData.get('password')
            
            # Customer Object 
            customer = Customer(first_name = firstname,
                last_name = lastname,
                email = email,
                password = password)
            
            # Validation procedure
            value = {
                'first_name' : firstname,
                'last_name' : lastname,
                'email' : email
            }
            
            error_message = Signup.validateCustomerDetails(customer)
            
            ## Checking with Error_Message
            if not error_message:
                print(firstname,lastname,email)
                
                # encryption of the PASSWORD
                customer.password = make_password(customer.password)
                
                ## SAVING THE customers DATA
                customer.register()
                return render(request,'signup.html',{'error' : error_message})
            else:
                data = {
                    'error' : error_message,
                    'values' : value
                }
                return render(request,'signup.html',data)
            
            ## to redirect it to any other page 
                # return redirect('index')

    def validateCustomerDetails(customer): 
        error_message = None
                
        if(not customer.first_name):
            error_message = "First name is Required"
        elif len(customer.first_name)<4:
            error_message = "First name should be more than 4 char"
        elif(not customer.last_name):
            error_message = "Last name is Required"
        elif len(customer.last_name)<4:
            error_message = "Last name should be more than 4 char"
        elif (not customer.email):
            error_message = "Email is Required"
        elif len(customer.email)<5:
            error_message = "Email should be more than 5 characters"
        elif (not customer.password):
            error_message = "Password is Required"
        elif len(customer.password)<6:
            error_message = "PASSWORD should be more than 6 characters"
        elif customer.emailExists():
            error_message = "Email address already registred .. try a diffrent email address"

        return error_message



#Login  
class Login(View):
    def get(self,request):
        return render(request,'login.html')

    def post(self,request):
        # POST request 
        email = request.POST.get('email')
        password = request.POST.get('password')
        error_message = None
        
        # customer object variable 
        customer = Customer.get_customer_by_email(email)
        # print(customer)
        
        if customer:
            flag = check_password(password , customer.password)
            if flag:
                # Note : we will not initialize the OBJECT to the SESSION straight away 
                # rather we will initialize a part/data in the OBJECT to the SESSION
                # Session creation 
                # request.session['customer'] = customer
                
                # initializing CustomerId and Email to the session 
                request.session['customer_id'] = customer.id
                request.session['email'] = customer.email
                
                return redirect('/')
            else:
                error_message = 'Email or password invalid !!'
        else:
            error_message = 'Email or password invalid !!'
        
        return render(request,'login.html',{'error' : error_message})



# Contacts
class Contact(View):
    def get(self,request):
        return render(request,'contact.html')
    
    def post(self,request):
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        description = request.POST.get('description')
        contact = Contact( name = name, phone = phone, email = email, description = description)
        contact.save()
        return render(request,'contact.html')



#Contact
# 

