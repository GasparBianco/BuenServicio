from django.shortcuts import render
from tables.models import Table
from .models import Order
from products.models import Product
from django.shortcuts import redirect
from django.contrib import messages
import win32print
import win32ui

def home(request):
    tables = Table.objects.all().order_by('number')
    return render(request, 'salepoint/home.html', {'tables': tables})

def table(request, table):
    table = Table.objects.get(number=table)
    order = Order.objects.filter(table=table.id)
    printers = win32print.EnumPrinters(win32print.PRINTER_ENUM_LOCAL, None, 1)
    printers_names = []
    for i in range(len(printers)):
        printers_names.append(printers[i][2])
    total = 0
    for i in order:
        total += i.total
    context = { 'table':table,
                'order': order,
                'total': total,
                'message': list(messages.get_messages(request)),
                'printers': printers_names}                
    
    return render(request, 'salepoint/table.html', context)

def order(request, table_number):

    quantity_list = request.POST.getlist('quantity')
    id_list = request.POST.getlist('id')
    table_id = Table.objects.get(id = request.POST.get('table-id'))
    Table.objects.filter(id = table_id.id).update(available=False)
    hprinter = win32ui.CreateDC()
    hprinter.CreatePrinterDC(request.POST.get('printer'))
    hprinter.StartDoc('Comanda')
    hprinter.StartPage()
    command = f"Mesa {table_number}"
    hprinter.TextOut(100,100,command)
    command = request.POST.get('comment')
    hprinter.TextOut(100,200,command)
    command = "Producto                    Cantidad"
    hprinter.TextOut(100,300,command)
    for i in range(len(request.POST.getlist('id'))):
        product = Product.objects.get(id=id_list[i])
        quantity = quantity_list[i]
        total = product.cost * int(quantity)
        if int(quantity) != 0:
            Order(product=product, quantity=int(quantity), table=table_id, total = total).save()
            
            
            command = f"{product.name}"
            hprinter.TextOut(100,300+100*(i+1),command)
            command = f"{quantity}"
            hprinter.TextOut(700,300+100*(i+1),command)

    hprinter.EndPage()
    hprinter.EndDoc()


    return redirect('table', table=table_number)

def reprint(request, table_number):
    table = Table.objects.get(number = table_number)
    order = Order.objects.filter(table=table.id)

    hprinter = win32ui.CreateDC()
    hprinter.CreatePrinterDC(win32print.GetDefaultPrinter())
    hprinter.StartDoc('Comanda')
    hprinter.StartPage()
    command = "Reimpresion"
    hprinter.TextOut(100,100,command)
    command = f"Mesa {table_number}"
    hprinter.TextOut(100,200,command)
    if request.POST.get('comment'):
        command = request.POST.get('comment')
        hprinter.TextOut(100,300,command)
    command = "Producto                    Cantidad"
    hprinter.TextOut(100,400,command)
    for i in range(len(order)):
        
            
        command = f"{order[i].product}"
        hprinter.TextOut(100,400+100*(i+1),command)
        command = f"{order[i].quantity}"
        hprinter.TextOut(700,400+100*(i+1),command)

    hprinter.EndPage()
    hprinter.EndDoc()


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