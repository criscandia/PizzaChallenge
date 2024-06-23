from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('pizzas/', views.pizzas, name='pizzas'),

    path('new-order/', views.new_order, name='new_order'),
    path('order-list/', views.order_list, name='order_list'),
    path('top-pizzas/', views.top_pizzas, name='top_pizzas'),
    path('edit-order/<int:order_id>/', views.edit_order, name='edit_order'),
    path('delete-order/<int:order_id>/', views.delete_order, name='delete_order'),
    path('top-clients/', views.top_clients, name='top_clients'),
    path('contact/', views.contact, name='contact'),
    # path('orders/', views.orders, name='orders'),
    # path('orders/<int:order_id>/', views.order, name='order'),
    # path('clients/', views.clients, name='clients'),
    # path('clients/<int:client_id>/', views.client, name='client'),
    path('new-client/', views.new_client, name='new_client'),
]