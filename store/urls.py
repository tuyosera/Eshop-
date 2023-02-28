from django import urls
from django.contrib import admin
from django.urls import path
from store import views
# from django.urls import url
from .views import Signup , Login , Contact 
# from store.views import signup , contact , login , Index
from store import views


urlpatterns = [
    path('', views.index, name='index'),
    # path('', Index.as_view() , name="index"),
    path('signup', Signup.as_view() , name='signup'),
    path('login', Login.as_view() , name='login'),
    path('contact', Contact.as_view() , name='contact')
    # path('', views.index, name='index'),
    # path('about', views.about, name='about'),
    # path('contact', views.contact, name='contact'),
    # path('signup', views.signup, name='signup'),
    # path('login', views.login, name='login'),
]



# import views
# ...
# url(r'^classroom$', views.school.klass, name="classroom"),