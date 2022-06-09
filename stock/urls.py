from django.urls import path

from stock import views


app_name='stock'
urlpatterns = [
    path('stock_', views.stock, name='stock-list'),
    path('stock/add', views.stock_form, name='stock-add'),
]
