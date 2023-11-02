from django.shortcuts import render, redirect
from .models import Cashier
from django.utils import timezone
from salepoint.models import Order
from tables.models import Table
from django.contrib import messages

# Create your views here.
def cashier(request):
    message = list(messages.get_messages(request))
    context = {'cashier': Cashier.objects.all(),
               'messages': message}
    return render(request, 'cashier/cashier.html', context)

def open_cashier(request):
    if Cashier.objects.latest('open_date').close_date == None:
        messages.info(request, "No se puede abrir una nueva caja sin cerrar la anterior")
        return redirect('cashier')
    new = Cashier(
    cashier_user=str(request.user.username),
    open_money=int(request.POST.get('open')),  
    theorical_money=int(request.POST.get('open')),
    )
    new.save()
    messages.info(request, 'Caja abierta correctamente')
    return redirect('cashier')

def close_cashier(request):
    update = Cashier.objects.latest('open_date')
    if update.close_date != None:
        messages.info(request, 'No hay ninguna caja abierta actualmente')
        return redirect('cashier')
    update.close_money = int(request.POST.get('close'))
    update.close_date = timezone.now()
    update.save()
    messages.info(request, 'Caja cerrada correctamente')
    return redirect('cashier')

def pay(request):
    update = Cashier.objects.latest('open_date')
    table_id = request.POST.get('table_id')
    if update.close_date != None:
        table = Table.objects.filter(id = table_id)
        messages.info(request, "No hay ninguna caja abierta actualmente")
        return redirect('table', table=table[0].number)
    

    discounts = request.POST.getlist('discount')
    discounts = [int(value) for value in discounts]
    order = Order.objects.filter(table=table_id).order_by('id').all()
    cost = []

    for i in range(len(discounts)):
        if discounts[i] >= 0 and discounts[i] <= 100:
            cost.append(order[i].total * (1 - discounts[i]/100))
    cost = sum(cost * (1 - request.POST.get('general-discount')/100))
    if request.POST.get('cash'):
        update = Cashier.objects.latest('open_date')
        update.theorical_money = cost +  update.theorical_money
        update.save()
    Order.objects.filter(table=table_id).delete()
    Table.objects.filter(id = table_id).update(available=True)
    return redirect('home')