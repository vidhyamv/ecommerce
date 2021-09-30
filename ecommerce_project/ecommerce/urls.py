from django.contrib import admin
from . import views
from django.urls import path

app_name='ecommerce'
urlpatterns = [
    path('',views.allprodcat,name='allprodcat'),
    path('<slug:c_slug>/',views.allprodcat,name='product_by_category'),
    path('<slug:c_slug>/<slug:product_slug>/',views.prodetail,name='procatdetail'),
]