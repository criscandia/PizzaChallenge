from itertools import count
from django.shortcuts import render, redirect 
from .models import Pizza, Client, Order
from .forms import ClientForm
from .forms import OrderForm
from django.db.models import Count


def index(request, template_name='index.html'):
    """The home page for Pizzeria."""
    return render(request, template_name)

def pizzas(request, template_name='pizzas.html'):
    """Show all pizzas."""
    pizza_list = Pizza.objects.all()
    dato = {'pizzas': pizza_list}
    return render(request, template_name, dato)

def clients(request, template_name='app/clients.html'):
    """Show a single pizza and its details."""
    client_list = Client.objects.all()
    dato = {'clients': client_list}
    return render(request, template_name, dato)

def new_client(request, template_name='new-client.html'):
    """Add a new client."""
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = ClientForm()
    else:
        # POST data submitted; process data.
        form = ClientForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    # Display a blank or invalid form.
    context = {'form': form}
    return render(request, template_name, context)

def client(request, client_id, template_name='app/client.html'):
    """Show a single client and its details."""
    client = Client.objects.get(id=client_id)
    dato = {'client': client}
    return render(request, template_name, dato)

def new_order(request, template_name='new-order.html'):
    """Add a new order."""
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = OrderForm()
    else:
        # POST data submitted; process data.
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('order_list')  # Ajusta esto a la URL de tu lista de pedidos o página de confirmación
    dato = {'form': form}
    return render(request, template_name, dato)

    # Display a blank or invalid form.
    context = {'form': form}
    return render(request, template_name, context)

def order_list(request, template_name='order-list.html'):
    """Show all orders."""
    order_list = Order.objects.all()
    dato = {'orders': order_list}
    return render(request, template_name, dato)

def order(request, order_id, template_name='app/order.html'):
    """Show a single order and its details."""
    order = Order.objects.get(id=order_id)
    dato = {'order': order}
    return render(request, template_name, dato)

def edit_order(request, order_id, template_name='edit-order.html'):
    """Edit an existing order."""
    order = Order.objects.get(id=order_id)
    if request.method != 'POST':
        # Initial request; pre-fill form with the current entry.
        form = OrderForm(instance=order)
    else:
        # POST data submitted; process data.
        form = OrderForm(instance=order, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('order_list')  # Ajusta esto a la URL de tu lista de pedidos o página de confirmación

    context = {'order': order, 'form': form}
    return render(request, template_name, context)

def delete_order(request, order_id, template_name='delete-order.html'):
    """Delete an existing order."""
    order = Order.objects.get(id=order_id)
    if request.method == 'POST':
        order.delete()
        return redirect('order_list')  # Ajusta esto a la URL de tu lista de pedidos o página de confirmación

    context = {'order': order}
    return render(request, template_name, context)

def top_pizzas(request, template_name='top-pizzas.html'):
    """Show the top pizzas and the top client."""
    pizzas = Pizza.objects.annotate(total_orders=Count('order')).order_by('-total_orders')[:5]
    # Obtiene el cliente con más órdenes. Usamos first() para obtener solo el primero.
    top_client = Client.objects.annotate(total_orders=Count('order')).order_by('-total_orders').first()
    dato = {'pizzas': pizzas, 'top_client': top_client}
    return render(request, template_name, dato)

def top_clients(request, template_name='app/top-clients.html'):
    """Show the top clients."""
    clients = Client.objects.annotate(total_orders=Count('order')).order_by('-total_orders')[:5]
    dato = {'clients': clients}
    return render(request, template_name, dato)

def contact(request, template_name='contact.html'):
    """Show the contact page."""
    return render(request, template_name)