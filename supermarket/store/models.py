from django.db import models


# Create your models here.

    
class category(models.Model):
    name=models.CharField(max_length=150,null=False,blank=False)
    image=models.ImageField(upload_to="category image",null=True,blank=True)
    status=models.BooleanField(default=False,help_text="0=default,1=Hidden")
    trending=models.BooleanField(default=False,help_text="0=default,1=Trending")
    date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class product(models.Model):
         name=models.CharField(max_length=100,null=False,blank=False)
         price=models.FloatField(null=False,blank=False)
         category=models.ForeignKey(category,on_delete=models.CASCADE)
         date=models.DateTimeField(auto_now_add=True)
         image=models.ImageField(upload_to="product_image",null=True,blank=True)
         status=models.BooleanField(default=False,help_text="0=default,1=Hidden")
         trending=models.BooleanField(default=False,help_text="0=default,1=Trending")
         def __str__(self):
          return self.name