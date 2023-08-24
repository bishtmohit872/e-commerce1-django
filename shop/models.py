from django.db import models

# Create your models here.
class signup(models.Model):
    user_id=models.AutoField
    user_name=models.CharField(max_length=20,default="")
    user_email=models.CharField(max_length=20,default="")
    user_password=models.CharField(max_length=15,default="")
    
    def __str__(self):
        return self.user_name

class product(models.Model):
    product_id=models.AutoField
    product_name=models.CharField(max_length=50,default="")
    category=models.CharField(max_length=50,default="")
    subcategory=models.CharField(max_length=50,default="")
    price=models.IntegerField(default=0)
    description=models.CharField(max_length=1000,default="")
    publish_date=models.DateField()
    image=models.ImageField(upload_to="shop/images",default="")
    
    def __str__(self):
        return self.product_name

class user_exist:   #checking the existance of user whether login or logout! 
    user:bool       # And no need to register on admin.py until its not inherited from "models.Model"

class contact(models.Model):
    msg_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50,default="")
    email=models.CharField(max_length=50,default="")
    contact_no=models.CharField(max_length=12,default="")
    query_type=models.CharField(max_length=100,default="")
    query_desc=models.CharField(max_length=100,default="")
    feedback=models.CharField(max_length=1000,default="")

    def __str__(self):
        return self.name

class orders(models.Model):
    order_id = models.AutoField(primary_key=True)
    items_json = models.CharField(max_length=5000)
    amount=models.IntegerField(default=0)
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=15)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=10)
    zip_code = models.CharField(max_length=10)
    phone = models.IntegerField(default=0)
    
    def __str__(self):
        return self.email

class orderupdate(models.Model):
    update_id=models.AutoField(primary_key=True)
    order_id=models.IntegerField(default="")
    update_desc=models.CharField(max_length=5000)
    timestamp=models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.update_desc[4:10]+str(self.order_id)
