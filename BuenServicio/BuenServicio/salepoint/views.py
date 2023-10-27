from django.shortcuts import render
from tables.models import Table
from .models import Order

def home(request):
    tables = Table.objects.all()
    return render(request, 'salepoint/home.html', {'tables': tables})

def table(request, table):
    context = {'table':Table.objects.get(number=table)}
    if request.method ==  'POST':
        print(request.POST)
    
    return render(request, 'salepoint/table.html', context)