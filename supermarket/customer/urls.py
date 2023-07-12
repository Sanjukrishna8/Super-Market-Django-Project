from django.urls import path
from .views import *
from . import views

urlpatterns=[
    path('chome',CustHomeView.as_view(),name="ch"),
    path('collections',collections.as_view(),name="collections"),
    path('products',products.as_view(),name="products"),
    path('acart/<int:pid>',Addcart.as_view(),name="acart"),
    path('viewcart',CartListView.as_view(),name="vcart"),
    path('delcart/<int:id>',deletecartitem,name="dcart"),
    path('check/<int:did>',checkoutview.as_view(),name="checkout"),
    path('orders',OrderView.as_view(),name='order'),
    path('cancelorder/<int:id>',cancel_order,name='orderc'),
    path('catpro/<int:id>',productview.as_view(),name="catpro"),
    path('search',Search.as_view(),name='search')
   
]