from django.urls import path
from . import views


# My route
urlpatterns = [
    # path('msg/', views.say_hello, name='message'),
    # path('home/', views.msg)
    path('', views.main, name="main"),
    path('products/', views.productFetch, name="products"),
    path('products/details/<int:id>', views.details, name="details")
]
