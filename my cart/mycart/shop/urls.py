
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name= "ShopHome"),
    path("about", views.about, name= "AboutUs"),
    path("contact", views.contact, name= "contactUs"),
    path("search", views.search, name= "Search"),
    path("tracker", views.tracker, name= "Tracker"),
    path("productView", views.productView, name= "ProductView"),
    path("checkout", views.checkout, name= "Checkout"),
    path("wishlist", views.wishlist, name= "Wishlist"),

]
