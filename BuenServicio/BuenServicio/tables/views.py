from django.shortcuts import render
from .models import Table
from .forms import OneTableForm, ManyTableForm
from django.db import IntegrityError

def addOneTable(request):
    form = OneTableForm(request.POST)
    try:
        form.is_valid()
        number = form.cleaned_data['number']
        new_table = Table(number=number)
        new_table.save() 
        confirmation = "La mesa se ha registrado correctamente"
    except IntegrityError:
        confirmation = "El numero ingresado ya existe o no es valido"
    tables = Table.objects.values_list('number', flat=True)
    context = {
        'tables':tables,
        'confirmation': confirmation,
        'one_table_form': OneTableForm(),
        'many_table_form': ManyTableForm()
        }
    return render(request, 'tables/gestion_mesas.html', context)

def addManyTables(request):
    form = ManyTableForm(request.POST)
    if form.is_valid():
        start = form.cleaned_data['start']
        end = form.cleaned_data['end'] + 1
        for number in range(start,end):
            try:
                new_table = Table(number=number)
                new_table.save() 
                confirmation = "La mesa se ha registrado correctamente"
            except IntegrityError:
                confirmation = "La mesa con ese número ya existe"
    else:
        confirmation = "Las mesas no se han podido registrar"

    tables = Table.objects.values_list('number', flat=True)
    context = {
        'tables':tables,
        'confirmation': confirmation,
        'one_table_form': OneTableForm(),
        'many_table_form': ManyTableForm()
        }
    return render(request, 'tables/gestion_mesas.html', context)

def deleteOneTable(request):
    number = request.POST.get('number')
    try:
        mesa = Table.objects.get(number=number)
        mesa.delete()
        confirmation = f"La mesa {number} ha sido eliminada"
    except Table.DoesNotExist:
        confirmation = f"No existe una mesa con el número {number}"
    tables = Table.objects.values_list('number', flat=True)
    context = {
        'tables':tables,
        'confirmation': confirmation,
        'one_table_form': OneTableForm(),
        'many_table_form': ManyTableForm()
        }
    return render(request, 'tables/gestion_mesas.html', context)

def gestion_mesas(request):
    tables = Table.objects.order_by('number').values_list('number', flat=True)
    context = {
        'tables':tables,
        'one_table_form': OneTableForm(),
        'many_table_form': ManyTableForm()
        }
    return render(request, 'tables/gestion_mesas.html', context)

def deleteAllTables(request):
    if 'delete' in request.POST:
        Table.objects.all().delete()
        confirmation = "Todas las mesas han sido eliminadas"
        tables = Table.objects.values_list('number', flat=True)
        context = {
        'tables':tables,
        'confirmation': confirmation,
        'one_table_form': OneTableForm(),
        'many_table_form': ManyTableForm()
        }
        return render(request, 'tables/gestion_mesas.html', context)
    return render(request, 'tables/delete_all_tables.html')