from django.shortcuts import render
from tables.models import Table
from .models import Order
from products.models import Product
from django.shortcuts import redirect
from django.contrib import messages

def home(request):
    tables = Table.objects.all().order_by('number')
    return render(request, 'salepoint/home.html', {'tables': tables})

def table(request, table):
    table = Table.objects.get(number=table)
    order = Order.objects.filter(table=table.id)
    total = 0
    for i in order:
        total += i.total
    context = { 'table':table,
                'order': order,
                'total': total,
                'message': list(messages.get_messages(request))}                
    
    return render(request, 'salepoint/table.html', context)

def order(request, table_number):

    quantity_list = request.POST.getlist('quantity')
    id_list = request.POST.getlist('id')
    table_id = Table.objects.get(id = request.POST.get('table-id'))
    Table.objects.filter(id = table_id.id).update(available=False)
    for i in range(len(request.POST.getlist('id'))):
        product = Product.objects.get(id=id_list[i])
        quantity = quantity_list[i]
        total = product.cost * int(quantity)
        if int(quantity) != 0:
            Order(product=product, quantity=int(quantity), table=table_id, total = total).save()
    return redirect('table', table=table_number)

def reset_table(request, table_number):
    
    table_id = Table.objects.get(number=table_number).id
    Order.objects.filter(table=table_id).delete()
    Table.objects.filter(id = table_id).update(available=True)
    return redirect('table', table=table_number)

def payment(request, table):
    table = Table.objects.get(number=table)
    order = Order.objects.filter(table=table.id)
    total = 0
    for i in order:
        total += i.total
    context = { 'table':table,
                'order': order,
                'total': total}   
    return render(request, 'salepoint/payment.html', context)