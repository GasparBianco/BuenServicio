from django.shortcuts import render, redirect
from .models import Cashier
from django.utils import timezone

# Create your views here.
def cashier(request, message = ''):
    context = {'message': message}
    context['cashier'] = Cashier.objects.all()
    return render(request, 'cashier/cashier.html', context)

def open_cashier(request):
    if Cashier.objects.latest('open_date').close_date == None:
        return redirect('cashier', message ='No se puede abrir una nueva caja sin cerrar la anterior')
    new = Cashier(
    cashier_user=str(request.user.username),
    open_money=int(request.POST.get('open')),  
    theorical_money=int(request.POST.get('open')),
    )
    new.save()
    return redirect('cashier',  message ='Caja abierta correctamente')

def close_cashier(request):
    update = Cashier.objects.latest('open_date')
    if update.close_date != None:
        return redirect('cashier',  message ='No hay ninguna caja abierta actualmente')
    update.close_money = int(request.POST.get('close'))
    update.close_date = timezone.now()
    update.save()
    return redirect('cashier',  message ='Caja cerrada correctamente')