from django.db import models

# Create your models here.
class Product(models.Model):
    product_id=models.AutoField
    product_name=models.CharField(max_length=50)
    category= models.CharField(max_length=50, default="")
    sub_category= models.CharField(max_length=50, default="")
    price=models.IntegerField(default=00)
    desc=models.CharField(max_length=300)
    pub_date=models.DateField()
    image= models.ImageField(upload_to="shop/images",default="")
    
    def __str__(self):
        return self.product_name
    
class Contact(models.Model):
    msg_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=65)
    email= models.CharField(max_length=80, default="")
    phone=models.CharField(max_length=50, default="")
    desc=models.CharField(max_length=500,default="")
    
    def __str__(self):
        return self.name
    
class Orders(models.Model):
    order_id=models.AutoField(primary_key=True)
    items_json = models.CharField(max_length=2000)
    amount = models.IntegerField(default=0)
    name = models.CharField(max_length=65)
    email = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zip = models.CharField(max_length=20)
    phone = models.CharField(max_length=30)
    
    def __str__(self):
        return self.name
    
class OrderUpdate(models.Model):
    update_id = models.AutoField(primary_key=True)
    order_id = models.IntegerField(default="")
    update_desc = models.CharField(max_length=500)
    time_stamp = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.update_desc[0:7] + "...."
    
    