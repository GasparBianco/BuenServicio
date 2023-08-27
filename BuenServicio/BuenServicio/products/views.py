from django.shortcuts import render
from .models import Product, ProductCategory
from .forms import ProductForm, ProductCategoryForm, FactorForm
from django.db import IntegrityError
from django.db.models import F
from django.core import serializers 
from django.http import JsonResponse

def addProduct(request):
    form = ProductForm(request.POST)
    if form.is_valid():
        try:        
            form.save() 
            confirmation = "El producto se ha registrado correctamente"
        except IntegrityError:
            confirmation = "El producto ingresado ya existe"
    else: 
        confirmation = "El costo de un producto debe ser mayor a 0"
    products = Product.objects.all()
    categories = ProductCategory.objects.all()
    context = {
        'categories': categories,
        'products':products,
        'confirmation': confirmation,
        'ProductForm': ProductForm(),
        'ProductCategoryForm': ProductCategoryForm()
        }
    
    return render(request, 'products/products.html', context)

def deleteOneProduct(request):
    id = request.POST.get('id')
    try:
        product = Product.objects.get(id=id)
        product.delete()
        confirmation = "El producto ha sido eliminado correctamente"
    except Product.DoesNotExist:
        confirmation = "No existe ese producto"
    products = Product.objects.all()
    categories = ProductCategory.objects.all()
    context = {
        'categories': categories,
        'products':products,
        'confirmation': confirmation,
        'ProductForm': ProductForm(),
        'ProductCategoryForm': ProductCategoryForm()
        }
    
    return render(request, 'products/products.html', context)


def deleteAllProducts(request):
    if 'delete' in request.POST:
        Product.objects.all().delete()
        confirmation = "Todos los productos han sido eliminados"
        products = Product.objects.all()
        categories = ProductCategory.objects.all()
        context = {
            'categories': categories,
            'products':products,
            'confirmation': confirmation,
            'ProductForm': ProductForm(),
            'ProductCategoryForm': ProductCategoryForm()
        }
        return render(request, 'products/products.html', context)
    return render(request, 'products/delete_all_products.html')


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


def updateOneProduct(request):
    id = request.POST.get('id')
    if 'update' in request.POST:
        try:
            product = Product.objects.get(id=id)
            form = ProductForm(request.POST, instance=product)
            if form.is_valid():
                form.save()
                confirmation = 'Producto actualizado correctamente'
            else:
                confirmation = "Los datos ingresados no son validos"
        except Product.DoesNotExist:
            confirmation = "No existe ese producto"            
        products = Product.objects.all()
        categories = ProductCategory.objects.all()
        context = {
            'categories': categories,
            'products':products,
            'confirmation': confirmation,
            'ProductForm': ProductForm(),
            'ProductCategoryForm': ProductCategoryForm()
        }
        return render(request, 'products/products.html', context)
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
        print(factor)
        form = FactorForm(request.POST)
        if form.is_valid():
            Product.objects.update(cost=F('cost') * factor)
            confirmation = "Precios actualizados con exito"
        else:
            confirmation = "El factor ingresado debe ser mayor a 0"
        products = Product.objects.all()
        categories = ProductCategory.objects.all()
        context = {
        'confirmation': confirmation,
        'categories': categories,
        'products':products,
        'ProductForm': ProductForm(),
        'ProductCategoryForm': ProductCategoryForm(),
        }
        return render(request, 'products/products.html', context)
    return render(request, 'products/update_all_products.html', {'FactorForm': FactorForm()})

def addCategory(request):
    form = ProductCategoryForm(request.POST)
    try:
        form.is_valid()
        form.save() 
        confirmation = "La categoria se ha registrado correctamente"
    except IntegrityError:
        confirmation = "La categoria ingresado ya existe o no es valido"
    products = Product.objects.all()
    categories = ProductCategory.objects.all()
    context = {
        'categories': categories,
        'products':products,
        'confirmation': confirmation,
        'ProductForm': ProductForm(),
        'ProductCategoryForm': ProductCategoryForm()
        }
    
    return render(request, 'products/products.html', context)


def deleteOneCategory(request):
    id = request.POST.get('id')
    try:
        category = ProductCategory.objects.get(id=id)
        category.delete()
        confirmation = "La categoria ha sido eliminado correctamente"
    except Product.DoesNotExist:
        confirmation = "No existe esa categoria"
    products = Product.objects.all()
    categories = ProductCategory.objects.all()
    context = {
        'categories': categories,
        'products':products,
        'confirmation': confirmation,
        'ProductForm': ProductForm(),
        'ProductCategoryForm': ProductCategoryForm()
        }
    
    return render(request, 'products/products.html', context)


def deleteAllCategories(request):
    if 'delete' in request.POST:
        ProductCategory.objects.all().delete()
        confirmation = "Todos las categorias han sido eliminadas"
        products = Product.objects.all()
        categories = ProductCategory.objects.all()
        context = {
            'categories': categories,
            'products':products,
            'confirmation': confirmation,
            'ProductForm': ProductForm(),
            'ProductCategoryForm': ProductCategoryForm()
        }
        return render(request, 'products/products.html', context)
    return render(request, 'products/delete_all_categories.html')

def search_products(request):
    query = request.GET.get('query', '')
    products = Product.objects.filter(name__icontains=query)
    products_data = serializers.serialize('json', products)
    return JsonResponse({'products': products_data})