from django.urls import path
from . import views

app_name='cart_app'
urlpatterns=[
    path('add/<int:product_id>/',views.add_cart,name='add_cart'),
    path('ele_a',views.cart_detail,name='cart_detail'),
    path('remove/<int:product_id>/',views.cart_remove,name='cart_remove'),
    path('delete/<int:product_id>/',views.cart_delete,name='cart_delete'),

]