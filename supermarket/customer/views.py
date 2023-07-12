from typing import Any, Dict
from django.db.models.query import QuerySet
from django.shortcuts import render,redirect
from django.views.generic import View
from store.models import category,product
from django.views.generic import View,TemplateView,ListView
from django.contrib import messages
from .models import Cart,Order
from django.db.models import Sum
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache

def signin_required(fn):
    def inner(request,*args,**kwargs):
        if request.user.is_authenticated:
           return fn(request,*args,**kwargs)
        else:
            messages.error(request,"please Login first")
            return redirect("log")
    return inner
dec=[signin_required,never_cache]



# Create your views here.
@method_decorator(dec,name="dispatch")
class CustHomeView(View):
    def get(self,request):
        return render(request,"admin_base.html")


# def collections(request):
#     cat=category.objects.filter(status=0)
#     context={'category':cat}
#     return render(request,"collections.html",context)
@method_decorator(dec,name="dispatch")
class collections(TemplateView):
    template_name="collections.html"

    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context["data"]=category.objects.all()
        return context
    
@method_decorator(dec,name="dispatch")
class products(TemplateView):
    template_name="products.html"

    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context["dat"]=product.objects.all()
        return context
    
@method_decorator(dec,name="dispatch")
class Addcart(View):
   def  get (self,request,*args,**kwargs):
       prod=product.objects.get(id=kwargs.get("pid"))
       user=request.user
       Cart.objects.create(product=prod,user=user)
       messages.success(request,"product Added to Cart  ")
       return redirect("products")
@method_decorator(dec,name="dispatch")  
class CartListView(ListView):
    template_name="cart-list.html"
    model=Cart
    context_object_name="cartitem"

    def get_queryset(self):
        cart=Cart.objects.filter(user=self.request.user,status="cart")
        total=Cart.objects.filter(user=self.request.user,status='cart').aggregate(tot=Sum("product__price"))
        return {"items":cart,"total":total}
dec    
def deletecartitem(request,id):
    cart=Cart.objects.get(id=id)
    cart.delete()
    messages.error(request,"Cart item Removed...")
    return redirect("vcart")

@method_decorator(dec,name="dispatch")
class checkoutview(View):
    def get(self,request,*args,**kwargs):
      return render(request,"checkout.html")
    def post(self,request,*args,**kwargs):
        id=kwargs.get("did")
        cart=Cart.objects.get(id=id)
        prod=cart.product
        user=request.user
        address=request.POST.get("address")
        phone=request.POST.get("phone")
        Order.objects.create(product=prod,user=user,address=address,phone=phone)
        cart.status="order placed"
        cart.save()
        messages.success(request,"Order placed Successfully....")
        return redirect("vcart")
    

@method_decorator(dec,name="dispatch")
class OrderView(ListView):
    template_name="orders.html"
    model= Order
    context_object_name="order"
    def get_queryset(self):
        order=Order.objects.filter(user=self.request.user)
        return {"order":order}
dec    
def cancel_order(request,id):
    order=Order.objects.get(id=id)
    order.status="cancel"
    order.save()
    messages.success(request,"order Cancelled")
    return redirect("order")
   

@method_decorator(dec,name="dispatch")
class productview(View):
   def get(self,request,*args,**kwargs):
     cid=kwargs.get("id")
     cat=category.objects.get(id=cid)
     pro=product.objects.filter(category=cat)
     return  render(request,"pro.html",{"pro":pro})


@method_decorator(dec,name="dispatch")
class Search(View):
    def get(self,request,*args,**kwargs):
        search=request.GET.get("search")
        products=product.objects.filter(name__icontains=search)
        context={"searchpro":products}
        return render (request,'search.html',context)

