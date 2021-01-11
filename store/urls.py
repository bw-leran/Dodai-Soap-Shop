from django.urls import path
from . import views

#maybe need these later?
#from django.contrib import admin
#from django.urls import path

urlpatterns = [
    path('',views.store,name='store'),
    path('cart/',views.cart,name='cart'),
    path('checkout/',views.checkout,name='checkout'),
    path('about/',views.about,name='about'),
    path('update_item/',views.updateItem,name='update_item'),
    path('process_order/',views.processOrder,name='process_order'),
    path('view/',views.view,name='view'),
    path('view/<int:prodId>', views.view, name='view'), #attempt to pass value through URL
]