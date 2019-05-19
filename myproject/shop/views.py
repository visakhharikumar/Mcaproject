import json

from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.template import RequestContext
from django.views.decorators.csrf import csrf_protect
from datetime import datetime

# Create your views here.
from .models import register, products, Cart, Address, Order, OrderDetail, OrderStatus

def logout(request):
        request.session['user_id']='';
        return HttpResponseRedirect("/login")
def login(request):
    if request.method == 'POST':
        # if not logged_in:
        un = request.POST['unm']
        pw = request.POST['psw']
        # print(un + pw )
        r_obj = register.objects.filter(username=un, password=pw).first()
        print('count :', r_obj)
        if r_obj:
            request.session['user_id'] = str(r_obj.id);
            return HttpResponseRedirect("/shop_home")
        else:
            # return  HttpResponse('hi'+request.POST['usnm'])
            # return HttpResponse('welcom to my shoap')
           return render(request, 'shop/login.html' , {'status': False, 'message': 'Invalid credentials.'} )    
    else:
        try:
            logged_in = request.session['user_id']
        except:
            logged_in = False
            request.session['user_id'] = None

        print("logged_in", logged_in)
        if logged_in:
            s = products.objects.all()
            categories = []
            brands = []
            types = []
            data = []
            for item in s:
                temp_object = {}
                temp_object['id'] = item.id
                temp_object['name'] = item.name
                temp_object['image'] = "../../" + str(item.image)[5:]
                temp_object['price'] = item.price
                temp_object['brand'] = item.brand
                if int(item.quantity):
                    temp_object['out_of_stock'] = False
                else:
                    temp_object['out_of_stock'] = True
                temp_object['quantity'] = item.quantity
                categories.append(item.category)
                brands.append(item.brand)
                types.append(item.type)
                data.append(temp_object)
            print('login called : '+logged_in)
            return  render(request,'shop/myshop.html', { 'products': data, 'types': types,'brands': brands,'categories': categories, })

        return render(request,'shop/login.html',{'status': True, 'message': ''})

def signup(request):
    if request.method=='POST':
        un=request.POST['unm']
        mail=request.POST['email']
        pw=request.POST['psw']
        obj=register(username=un,email=mail,password=pw)
        obj.save()
        r_obj = register.objects.filter(username=un, password=pw).first()

        #return render(request,'shop/myshop.html')
        request.session['user_id'] = str(r_obj.id);
        return HttpResponseRedirect("/shop_home")
    else:
        #return render(request,'shoap/signup.html')class="btn btn-default"
        return HttpResponse('provide valid details')

def shop_home(request):
    try:
        logged_in = request.session['user_id']
    except:
        logged_in = False

    print("logged_in", logged_in)

    s = products.objects.all()
    categories = []
    brands = []
    types = []
    data = []
    for item in s:
        temp_object = {}
        temp_object['id'] = item.id
        temp_object['name'] = item.name
        temp_object['image'] = "../../" + str(item.image)[5:]
        temp_object['price'] = item.price
        temp_object['brand'] = item.brand
        if int(item.quantity):
            temp_object['out_of_stock'] = False
        else:
            temp_object['out_of_stock'] = True
        temp_object['quantity'] = item.quantity
        if item.category not in categories:
            categories.append(item.category)
        if item.category not in brands:
            brands.append(item.brand)
        if item.category not in types:
            types.append(item.type)
        data.append(temp_object)

    return  render(request,'shop/myshop.html', { 'products': data, 'types': types,'brands': brands,'categories': categories,'logged_in':logged_in })

def category_view(request,cat):
    try:
        logged_in = request.session['user_id']
    except:
        logged_in = False

    print("logged_in", logged_in)

    s = products.objects.filter(category=cat)
    categories = []
    brands = []
    types = []
    data = []
    for item in s:
        temp_object = {}
        temp_object['id'] = item.id
        temp_object['name'] = item.name
        temp_object['image'] = "../../" + str(item.image)[5:]
        temp_object['price'] = item.price
        temp_object['brand'] = item.brand
        categories.append(item.category)
        brands.append(item.brand)
        types.append(item.type)
        data.append(temp_object)

    return  render(request,'shop/myshop.html', { 'products': data, 'types': types,'brands': brands,'categories': categories, })

def types_view(request,ty):
    try:
        logged_in = request.session['user_id']
    except:
        logged_in = False

    print("logged_in", logged_in)

    s = products.objects.filter(type=ty)
    categories = []
    brands = []
    types = []
    data = []
    for item in s:
        temp_object = {}
        temp_object['id'] = item.id
        temp_object['name'] = item.name
        temp_object['image'] = "../../" + str(item.image)[5:]
        temp_object['price'] = item.price
        temp_object['brand'] = item.brand
        categories.append(item.category)
        brands.append(item.brand)
        types.append(item.type)
        data.append(temp_object)

    return  render(request,'shop/myshop.html', { 'products': data, 'types': types,'brands': brands,'categories': categories, })

def brand_view(request,bran):
    try:
        logged_in = request.session['user_id']
    except:
        logged_in = False

    print("logged_in", logged_in)

    s = products.objects.filter(brand=bran)
    categories = []
    brands = []
    types = []
    data = []
    for item in s:
        temp_object = {}
        temp_object['id'] = item.id
        temp_object['name'] = item.name
        temp_object['image'] = "../../" + str(item.image)[5:]
        temp_object['price'] = item.price
        temp_object['brand'] = item.brand
        categories.append(item.category)
        brands.append(item.brand)
        types.append(item.type)
        data.append(temp_object)

    return  render(request,'shop/myshop.html', { 'products': data, 'types': types,'brands': brands,'categories': categories, })

def checkout(request):
    try:
        logged_in = request.session['user_id']
    except:
        logged_in = False
    print("logged_in", logged_in)

    if request.method=='POST':
        uid=logged_in
        nm=request.POST['cnm']
        fn=request.POST['fnm']
        ln=request.POST['lnm']
        add1=request.POST['ad1']
        add2=request.POST['ad2']
        pinc=request.POST['pin']
        phn=request.POST['mob']
        payment_method=request.POST['payment_method']
        user = register.objects.filter(id=logged_in).first()

        address = Address(userid=user,fname=fn,lname=ln,hm_name=nm,address1=add1,address2=add2,pincode=pinc,mobile=phn)
        address.save()

        db_order_status = OrderStatus.objects.filter(id=1).first()

        order = Order(userid=user, address_id=address, created=datetime.now(), payment_method=payment_method, status=db_order_status)
        order.save()

        user_cart = Cart.objects.filter(userid=logged_in).all()
        total = 0.0
        for item in user_cart:
            order_detail = OrderDetail(order_id=order, product_id=item.product_id, quantity=item.quantity, price=item.product_id.price)
            # updating the stock
            db_product = products.objects.filter(id=item.product_id.id).first()
            new_quantity = int(db_product.quantity) - int(item.quantity)
            db_product.quantity=new_quantity
            db_product.save()
            # saving order detail
            order_detail.save()
            total = total + float(item.product_id.price)

        Order.objects.filter(id=order.id).update(amount=str(total))

        Cart.objects.filter(userid=logged_in).delete()

        return render(request, 'shop/confirm.html')
    # return  render(request,'shop/checkout.html')
    else:
        s1 = Cart.objects.filter(userid=logged_in).all()
        data = []
        total = 0.0
        for item in s1:
            temp_object = {}
            temp_object['id'] = item.id
            temp_object['name'] = item.product_id.name
            temp_object['brand'] = item.product_id.brand
            temp_object['image'] = "../../" + str(item.product_id.image)[5:]
            temp_object['price'] = item.product_id.price
            total = total + float(item.product_id.price)
            data.append(temp_object)
        return render(request, 'shop/checkout.html', { 'cart': data, 'total': total })

def order(request):
    print('order')
    try:
        logged_in = request.session['user_id']
    except:
        logged_in = False
    s1 = Order.objects.filter(userid=logged_in).all()
    data = []
    total = 0.0
    i='Delivered'
    for item in s1:
        temp_object = {}
        temp_object['id'] = item.id
        temp_object['address_id'] = item.address_id
        temp_object['status'] = item.status.status_text
        if (item.status.status_text !="Delivered"):
            temp_object['delivery'] = False
        else:
            temp_object['delivery'] = True
        temp_object['status_text'] = item.status_text
        temp_object['amount'] = item.amount
        # temp_object['image'] = "../../" + str(item.product_id.image)[5:]
        temp_object['payment_method'] = item.payment_method
        temp_object['created'] = item.created
        total = total + float(item.amount)
        data.append(temp_object)
        print(data)
    return render(request, 'shop/order-list.html', {'order': data, 'total': total})

def order_details(request,itmid):
    print('order')
    try:
        logged_in = request.session['user_id']
    except:
        logged_in = False
    s1 = OrderDetail.objects.filter(order_id=itmid).all()
    data = []
    total = 0.0

    for item in s1:
        temp_object = {}
        temp_object['id'] = item.order_id
        temp_object['product_id'] = item.product_id
        temp_object['name'] = item.product_id.name
        temp_object['brand'] = item.product_id.brand
        temp_object['image'] = "../../" + str(item.product_id.image)[5:]
        temp_object['price'] = item.product_id.price
        temp_object['status_text'] = item.order_id.status_text
        temp_object['status'] = item.order_id.status.status_text
        temp_object['payment_method'] = item.order_id.payment_method

        total = total + float(item.product_id.price)
        data.append(temp_object)
        print(data)
    return render(request, 'shop/order-detail.html', {'order_details': data, 'total': total})

def invoice(request,odid):
    print('order')
    try:
        logged_in = request.session['user_id']
    except:
        logged_in = False
    s1 = Order.objects.filter(id=odid).all()
    s2 = OrderDetail.objects.filter(order_id=odid).all()
    itm = []
    data = []
    total = 0.0

    for item in s1:
        temp_object = {}
        temp_object['id'] = item.id
        temp_object['address_id'] = item.address_id
        temp_object['offc']=item.address_id.hm_name
        temp_object['fname'] = item.address_id.fname
        temp_object['lname'] = item.address_id.lname
        temp_object['hm_name'] = item.address_id.hm_name
        temp_object['address1'] = item.address_id.address1
        temp_object['address2'] = item.address_id.address2
        temp_object['pincode'] = item.address_id.pincode
        temp_object['mobile'] = item.address_id.mobile
        temp_object['payment_method'] = item.payment_method
        data.append(temp_object)
        print(data)

    for item1 in s2:
        temp_object = {}
        temp_object['id'] = item1.order_id
        temp_object['product_id'] = item1.product_id
        temp_object['name'] = item1.product_id.name
        temp_object['brand'] = item1.product_id.brand
        temp_object['price'] = item1.product_id.price
        total = total + float(item1.product_id.price)
        itm.append(temp_object)

    return render(request, 'shop/invoice.html', { 'inv': data, 'inv1':itm, 'total': total })

# @csrf_protect
def delete_cart(request):
    # csrfContext = RequestContext(request)
    try:
        logged_in = request.session['user_id']
    except:
        logged_in = False
    if request.method == 'POST':
        print("logged_in", logged_in)
        cart_id = request.POST['cart_id']
        print("cart_id", cart_id)

        Cart.objects.filter(id=cart_id, userid=logged_in).delete()

        return HttpResponseRedirect("/cart")

def cart(request):
    # csrfContext = RequestContext(request)
    try:
        logged_in = request.session['user_id']
    except:
        logged_in = False
    if request.method == 'POST':
       

        print("logged_in", logged_in)
        product_id = request.POST['product_id']
        print("product_id", product_id)

        if logged_in:
            print ('logged_in:'+logged_in)
            obj=Cart(userid=register.objects.filter(id=logged_in).first(),product_id=products.objects.filter(id=product_id).first(), quantity=1)
            obj.save()
            print(' logged : aaaaaaaaaaaaaaaaaa')
            # return render(request, 'shop/cart.html')
            response = json.dumps({'logged_in':True})
            return JsonResponse(response, safe=False)
            #return HttpResponseRedirect("/cart")
        else:
            response=json.dumps({'logged_in':False})
            return  JsonResponse(response,safe=False)
            print('not logged : aaaaaaaaaaaaaaaaa')
            #return HttpResponseRedirect("/login")
            # return render(request, 'shop/login.html' , {'status': False, 'message': 'Login to continue.'} ) 
    else:
        s1 = Cart.objects.filter(userid=logged_in).all()
        data = []
        total = 0.0
        for item in s1:
            temp_object = {}
            temp_object['id'] = item.id
            temp_object['name'] = item.product_id.name
            temp_object['brand'] = item.product_id.brand
            temp_object['image'] = "../../" + str(item.product_id.image)[5:]
            temp_object['price'] = item.product_id.price
            total = total + float(item.product_id.price)
            data.append(temp_object)
        return render(request, 'shop/cart.html', { 'cart': data, 'total': total })


def payment(request):
    return render(request, 'shop/payment.html')

def purchase(request):
    return render(request, 'shop/confirm.html')

