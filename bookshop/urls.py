from bookshop.views import *
from django.urls import path

urlpatterns = [
    path('products/', ProductList.as_view()),
    path('products/<int:pk>/', ProductDetail.as_view())
]
