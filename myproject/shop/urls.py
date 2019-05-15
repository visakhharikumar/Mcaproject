from django.urls import path

from . import views
app_name='shop'
urlpatterns=[
    path('',views.login,name='login'),
    path('login/',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    # path('home/', views.home, name='homepage'),
    path('signup/', views.signup, name='reg'),
    path('shop_home/',views.shop_home, name='s_home'),
    path('cart/',views.cart, name='user_cart'),
    path('delete-cart/',views.delete_cart, name='user_cart_delete'),
    path('checkout/',views.checkout, name='user_checkout'),
    path('order/',views.order, name='user_orders'),
    path('payment/',views.payment, name='user_payment'),
    path('category/<str:cat>',views.category_view, name='prod_category'),
    path('types/<str:ty>', views.types_view, name='prod_types'),
    path('brands/<str:bran>', views.brand_view, name='prod_brand'),
    path('ord_info/<int:itmid>', views.order_details, name='order_info'),
    path('purchase/', views.purchase, name='purchase'),
    path('invoice/<int:odid>', views.invoice, name='user_invoice'),

]