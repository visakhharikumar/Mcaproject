from django.urls import path

from . import views
app_name='shop'
urlpatterns=[
    path('',views.login,name='index'),
    path('login/',views.login,name='login'),
    # path('home/', views.home, name='homepage'),
    path('signup/', views.signup, name='reg'),
    path('shop_home/',views.shop_home, name='s_home'),
    path('cart/',views.cart, name='user_cart'),
]