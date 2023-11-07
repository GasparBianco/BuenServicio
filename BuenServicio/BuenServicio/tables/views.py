from django.shortcuts import render, redirect
from .models import Table
from .forms import OneTableForm, ManyTableForm
from django.db import IntegrityError
from django.contrib import messages
from django.db.models.deletion import ProtectedError

def addOneTable(request):
    form = OneTableForm(request.POST)
    try:
        form.is_valid()
        number = form.cleaned_data['number']
        new_table = Table(number=number)
        new_table.save() 
        confirmation = "La mesa se ha registrado correctamente"
        messages.success(request, confirmation)
    except IntegrityError:
        confirmation = "El numero ingresado ya existe o no es valido"
        messages.error(request, confirmation)
    return redirect('tables')

def addManyTables(request):
    form = ManyTableForm(request.POST)
    if form.is_valid():
        start = form.cleaned_data['start']
        end = form.cleaned_data['end'] + 1
        for number in range(start,end):
            try:
                new_table = Table(number=number)
                new_table.save() 
                confirmation = "Mesas registradas correctamente"
                messages.success(request, confirmation)
            except IntegrityError:
                confirmation = "La mesa con ese número ya existe"
                messages.error(request, confirmation)
    else:
        confirmation = "Las mesas no se han podido registrar"
        messages.error(request, confirmation)
    return redirect('tables')

def deleteOneTable(request):
    number = request.POST.get('number')
    try:
        mesa = Table.objects.get(number=number)
        mesa.delete()
        confirmation = f"La mesa {number} ha sido eliminada"
        messages.success(request, confirmation)
    except Table.DoesNotExist:
        confirmation = f"No existe una mesa con el número {number}"
        messages.error(request, confirmation)
    return redirect('tables')

def gestion_mesas(request):
    tables = Table.objects.order_by('number').values_list('number', flat=True)
    context = {
        'tables':tables,
        'one_table_form': OneTableForm(),
        'many_table_form': ManyTableForm()
        }
    return render(request, 'tables/gestion_mesas.html', context)

def deleteAllTables(request):
    try:
        Table.objects.all().delete()
        confirmation = "Todas las mesas han sido eliminadas"
        messages.success(request, confirmation)
    except ProtectedError:
        confirmation = "No se han podido eliminar debido a mesas abiertas"
        messages.error(request, confirmation)
    return redirect('tables')
