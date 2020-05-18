from django.contrib import admin
from django.urls import path

from shop import views

urlpatterns = [
    path('',views.index,name="index"),
    path('shop/<int:id>',views.productView,name="productview"),
    path('contact/',views.contact,name="contact"),
    path('about/',views.about,name="about")

]
