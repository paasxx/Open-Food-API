from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('token', obtain_auth_token, name='token'),
    path('products', views.getFoods, name='products'),
    path('product/create', views.addFood, name='create'),
    path('product/<str:pk>', views.methodFood, name='product_id'),
    path('product/<str:pk>', views.methodFood, name='update'),
    path('product/<str:pk>', views.methodFood, name='delete'),

]