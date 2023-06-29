from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.

class Customer(models.Model):
    user = models.OneToOneField(User, null=True, blank=True,on_delete=models.CASCADE)
    name = models.CharField(max_length=255,blank=True, null=True)
    email = models.CharField(max_length=255)

    # USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = ['name']

    def __str__(self):
         return self.name

class Brand(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255,unique=True)

    class Meta:
        verbose_name_plural = 'brands'
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("brand_list", args=[self.slug])
    
    
class Product(models.Model):
    name = models.CharField(max_length=255)
    brand = models.ForeignKey(Brand,on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='images/')
    slug = models.SlugField(max_length=255,unique=True)
    price = models.DecimalField(max_digits=5,decimal_places=2)
    # in_stock = models.BooleanField()
    # womens = models.BooleanField()
    def __str__(self):
            return self.name

    def get_absolute_url(self):
        return reverse("product_detail", args=[self.slug])
    
class Order(models.Model):
     customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
     date_ordered = models.DateTimeField(auto_now_add=True)
     complete = models.BooleanField(default=False)
     transaction_id = models.CharField(max_length=200,null=True)
    
     def __str__(self):
        return str(self.id)
     
     @property
     def shipping(self):
         shipping  = False
         orderitems = self.orderitem_set.all()
         for i in orderitems:
             shipping = True
         return shipping
     
     @property
     def get_cart_total(self):
         orderitems= self.orderitem_set.all()
         total = sum([item.get_total for item in orderitems])
         return total
     @property
     def get_cart_items(self):
         orderitems= self.orderitem_set.all()
         total = sum([item.quantity for item in orderitems])
         return total
     
class OrderItem(models.Model):
    product = models.ForeignKey(Product,on_delete=models.SET_NULL,blank=True,null=True)
    order = models.ForeignKey(Order,on_delete=models.SET_NULL,blank=True,null=True)
    quantity = models.IntegerField(default=0)
    date_added = models.DateTimeField(auto_now_add=True)
    shoe_size = models.IntegerField(null=True,blank=True)
    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total

class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.SET_NULL,blank=True,null=True)
    order = models.ForeignKey(Order,on_delete=models.SET_NULL,blank=True,null=True)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    zipcode = models.CharField(max_length=255)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address
