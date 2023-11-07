from django.shortcuts import render, redirect
from .models import Product, ProductCategory
from .forms import ProductForm, ProductCategoryForm, FactorForm
from django.db import IntegrityError
from django.db.models import F
from django.core import serializers 
from django.http import JsonResponse
from django.db.models.deletion import ProtectedError
from django.contrib import messages

def addProduct(request):
    form = ProductForm(request.POST)
    if form.is_valid():
        try:        
            form.save() 
            confirmation = "El producto se ha registrado correctamente"
            messages.success(request, confirmation)
        except IntegrityError:
            confirmation = "El producto ingresado ya existe"
            messages.error(request, confirmation)
    else: 
        confirmation = "El costo de un producto debe ser mayor a 0"
        messages.error(request, confirmation)
    return redirect('products')

def deleteOneProduct(request, id:int):
    try:
        product = Product.objects.get(id=id)
        product.delete()
        confirmation = "El producto ha sido eliminado correctamente"
        messages.success(request, confirmation)
    except Product.DoesNotExist:
        confirmation = "No existe ese producto"
        messages.error(request, confirmation)
    except ProtectedError:
        confirmation = "No se puede eliminar debido a una mesa abierta con ese producto"
        messages.error(request, confirmation)
    return redirect('products')


def deleteAllProducts(request):
    try:
        Product.objects.all().delete()
        confirmation = "Todos los productos han sido eliminados"
        messages.success(request, confirmation)
    except ProtectedError:
        confirmation = "No se puede eliminar debido a mesas abiertas"
        messages.error(request, confirmation)
    return redirect('products')


def products(request):
    products = Product.objects.all()
    categories = ProductCategory.objects.all()
    context = {
        'categories': categories,
        'products':products,
        'ProductForm': ProductForm(),
        'ProductCategoryForm': ProductCategoryForm()
        }
    
    return render(request, 'products/products.html', context)


def updateOneProduct(request, id:int):
    if 'update' in request.POST:
        try:
            product = Product.objects.get(id=id)
            form = ProductForm(request.POST, instance=product)
            if form.is_valid():
                form.save()
                confirmation = 'Producto actualizado correctamente'
                messages.success(request, confirmation)
            else:
                confirmation = "Los datos ingresados no son validos"
                messages.error(request, confirmation)
        except Product.DoesNotExist:
            confirmation = "No existe ese producto"
            messages.error(request,confirmation)
        return redirect('products')
    product = Product.objects.get(id=id)
    form = ProductForm(initial={
        'name': product.name, 
        'cost': product.cost, 
        'category': product.category
        })
    context = {
        'ProductForm': form,
        'product': product
    }
    return render(request, 'products/update_one_product.html', context)

def updateAllProducts(request):

    if 'update' in request.POST:
        factor = request.POST.get('factor')
        form = FactorForm(request.POST)
        if form.is_valid():
            Product.objects.update(cost=F('cost') * float(factor))
            confirmation = "Precios actualizados con exito"
            messages.success(request,confirmation)
        else:
            confirmation = "El factor ingresado debe ser mayor a 0"
            messages.error(request,confirmation)
        return redirect('products')
    return render(request, 'products/update_all_products.html', {'FactorForm': FactorForm()})

def addCategory(request):
    form = ProductCategoryForm(request.POST)
    try:
        form.is_valid()
        form.save() 
        confirmation = "La categoria se ha registrado correctamente"
        messages.success(request,confirmation)
    except IntegrityError:
        confirmation = "La categoria ingresado ya existe o no es valido"
        messages.error(request, confirmation)
    return redirect('products')


def deleteOneCategory(request):
    id = request.POST.get('id')
    try:
        category = ProductCategory.objects.get(id=id)
        category.delete()
        confirmation = "La categoria ha sido eliminado correctamente"
        messages.success(request, confirmation)
    except Product.DoesNotExist:
        confirmation = "No existe esa categoria"
        messages.error(request, confirmation)
    except ProtectedError:
        confirmation = "No se puede eliminar debido a productos con esa categoria"
        messages.error(request, confirmation)
    return redirect('products')


def deleteAllCategories(request):
    ProductCategory.objects.all().delete()
    confirmation = "Todos las categorias han sido eliminadas"
    messages.info(request, confirmation)
    return redirect('products')

def search_products(request):
    query = request.GET.get('query', '')
    products = Product.objects.filter(name__icontains=query)
    products_data = serializers.serialize('json', products)
    return JsonResponse({'products': products_data})