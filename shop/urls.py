from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='AboutUs'),
    path('contact/', views.contact, name='ContactUS'),
    path('tracker/', views.tracker, name='TrackingStatus'),
    path('search/', views.search, name='Search'),
    path("products/<int:myid>", views.productView, name="ProductView"),
    path('checkout/', views.checkout, name='Checkout'),
    path('success/', views.success, name='success'),
    path('cancle/', views.cancle, name='cancle'),
    
   ]
