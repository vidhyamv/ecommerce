from . import views
from django.urls import path

app_name='cart'

urlpatterns = [
    path('add/<int:product_id>/',views.add_cart,name='add_cart'),
    path('',views.Cartdetail,name='cart_detail'),
    path('remove/<int:product_id>/',views.cartremove,name='cart_remove'),
    path('delete/<int:product_id>/',views.cartdelete,name='cart_delete'),
]