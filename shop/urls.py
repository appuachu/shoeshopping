from django.urls import path
from . import views
urlpatterns = [
   path('',views.shop,name="shop"),
   path('<slug:c_slug>/',views.shop,name='prod_cat'),
   path('details/<int:pk>/',views.shopdetails.as_view(),name='details'),
   path('search',views.searching,name="search"),
   path('cart/<int:pk>/',views.cartview.as_view(),name="cart"),
   path('orderview',views.orderview,name="orderview"),
]