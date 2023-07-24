
from django.urls import path
from . import views

app_name = 'ecommerceapp'

urlpatterns = [
    path('', views.allproductcat, name='allproductcat'),
    path('<slug:c_slug>/', views.allproductcat, name='product_by_category'),
    path('<slug:c_slug>/<slug:product_slug>/', views.product_detail, name='product_detail'),
     path('', views.home_page, name='home'),
]
