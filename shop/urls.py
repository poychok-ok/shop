from django.urls import path
from shop.views import *


urlpatterns = [
    path('', catalog),
    path('product_detail/<int:product_id>/',product_detail),
    path('ordes/', ordes),
    path('create_ordes/<int:product_id>/', create_ordes)
]









