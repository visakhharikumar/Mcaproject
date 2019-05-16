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


class Address(models.Model):
    userid=models.ForeignKey(register, on_delete=models.CASCADE)
    fname=models.CharField(max_length=50)
    lname=models.CharField(max_length=50)
    hm_name=models.CharField(max_length=50)
    address1=models.CharField(max_length=50)
    address2=models.CharField(max_length=50)
    pincode=models.CharField(max_length=6)
    mobile=models.CharField(max_length=10)

    def __str__(self):
        return  str(self.id)

class OrderStatus(models.Model):
    status_text = models.CharField(max_length=100, default="Order Placed")

    def __str__(self):
        return str(self.status_text)


class Order(models.Model):
    userid = models.ForeignKey(register, on_delete=models.CASCADE)
    address_id = models.ForeignKey(Address, on_delete=models.CASCADE)
    amount =models.CharField(max_length=10)
    payment_method=models.CharField(max_length=50)
    status_text = models.CharField(max_length=50, default="Order Placed")
    status = models.ForeignKey(OrderStatus, on_delete=models.CASCADE, null=True)
    created=models.DateTimeField(auto_now=True)
    updated=models.DateTimeField(auto_now=True)

    def __str__(self):
        return  str(self.id)

class OrderDetail(models.Model):
    order_id=models.ForeignKey(Order, on_delete=models.CASCADE)
    product_id=models.ForeignKey(products, on_delete=models.CASCADE)
    quantity=models.CharField(max_length=50)
    price=models.CharField(max_length=50)

    def __str__(self):
        return str(self.id)


