from django.shortcuts import render
from tables.models import Table
from .models import Order
from products.models import Product

def home(request):
    tables = Table.objects.all()
    return render(request, 'salepoint/home.html', {'tables': tables})

def table(request, table):
    context = {'table':Table.objects.get(number=table)}
    if request.method ==  'POST':
        print(request.POST)
        quantity_list = request.POST.getlist('quantity')
        id_list = request.POST.getlist('id')
        for i in range(len(request.POST.getlist('id'))):
            product = Product.objects.get(id=id_list[i])
            table = Table.objects.get(id = request.POST.get('table-id'))
            quantity = quantity_list[i]
            if int(quantity) != 0:
                Order(product=product, quantity=int(quantity), table=table).save()
                
    
    return render(request, 'salepoint/table.html', context)