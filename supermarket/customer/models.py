from django.db import models
from store.models import product
from django.contrib.auth.models import User
# Create your models here.
class Cart(models.Model):
    product=models.ForeignKey(product,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    date=models.DateField(auto_now_add=True)
    status=models.CharField(max_length=100,default="cart")
    count=models.IntegerField(default=1)

    @property
    def qtyprice(self):
         tot=self.product.price*self.count
         return tot


class Order(models.Model):
     product=models.ForeignKey(product,on_delete=models.CASCADE)
     user=models.ForeignKey(User,on_delete=models.CASCADE)
     phone=models.IntegerField()
     address=models.CharField(max_length=500)
     options=(
          ("order placed","order placed"),
          ("shipped","shipped"),
          ("out for delivery","out for delivery"),
          ("Delivered","Delivered"),
          ("cancel","cancel")
     )
     status=models.CharField(max_length=100,choices=options,default="Order placed")
     date=models.DateField(auto_now_add=True)