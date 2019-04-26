from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import RequestContext
from django.views.decorators.csrf import csrf_protect


# Create your views here.
from .models import register, products, Cart


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
        # return render(request, 'shop/login.html')
        request.session['user_id'] = None
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
        #return render(request,'shoap/signup.html')
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
        categories.append(item.category)
        brands.append(item.brand)
        types.append(item.type)
        data.append(temp_object)

    return  render(request,'shop/myshop.html', { 'products': data, 'types': types,'brands': brands,'categories': categories, })

# @csrf_protect
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
            #add to cart
            #uid=request.session['user_id']
            #pid=request.session['product_id']
            obj=Cart(userid=register.objects.filter(id=logged_in).first(),product_id=products.objects.filter(id=product_id).first())
            obj.save()
    
            # return render(request, 'shop/cart.html')
            return HttpResponseRedirect("/cart")
        else:

            return HttpResponseRedirect("/login")
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