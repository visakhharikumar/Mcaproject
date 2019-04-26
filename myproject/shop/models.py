from django.db import models

# Create your models here.
class register(models.Model):
    username=models.CharField(max_length=50)
    email= models.CharField(max_length=50)
    password=models.CharField(max_length=50)

    def __str__(self):
        return self.username

class products(models.Model):
    id=models.CharField(primary_key=True,max_length=50)
    type=models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    subcategory = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    brand = models.CharField(max_length=50)
    price=models.CharField(max_length=50)
    quantity = models.CharField(max_length=50)
    image = models.ImageField(upload_to='shop/static/images/home/', default='shop/static/images/home/gallery2.jpg')

    def __str__(self):
        return self.id

class Cart(models.Model):
    userid=models.ForeignKey(register, on_delete=models.CASCADE)
    product_id=models.ForeignKey(products, on_delete=models.CASCADE)
    quantity=models.CharField(max_length=50)

    def __str__(self):
        return str(self.userid)

class Checkout(models.Model):
    checkout_id=models.CharField(primary_key=True, max_length=50)
    userid=models.ForeignKey(register, on_delete=models.CASCADE)
    product_id=models.ForeignKey(products, on_delete=models.CASCADE)
    fname=models.CharField(max_length=50)
    lname=models.CharField(max_length=50)
    hm_name=models.CharField(max_length=50)
    address1=models.CharField(max_length=50)
    address2=models.CharField(max_length=50)
    pincode=models.CharField(max_length=6)
    mobile=models.CharField(max_length=10)

    def __str__(self):
        return  str(self.checkout_id)

class Order(models.Model):
    order_id=models.CharField(max_length=50)
    userid = models.ForeignKey(register, on_delete=models.CASCADE)
    product_id = models.ForeignKey(products, on_delete=models.CASCADE)
    amount=models.CharField(max_length=10)
    pay_method=models.CharField(max_length=50)

    def __str__(self):
        return  str(self.order_id)


