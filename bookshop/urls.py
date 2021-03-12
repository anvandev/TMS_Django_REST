from django.urls import path
from bookshop.views import *

urlpatterns = [
    path('products/', ProductList.as_view()),
    path('products/<int:pk>/', ProductDetail.as_view())
]
