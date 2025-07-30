from django.urls import path
from . import views

urlpatterns=[
    path("productList/", views.product_list,name="product.list"),
    path("product/<int:id>/", views.product, name="product.product")
]