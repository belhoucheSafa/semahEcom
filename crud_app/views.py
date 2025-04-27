from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Product, Supplier
from .forms import ProductForm, SupplierForm
from django.contrib import messages

@login_required
def home(request):
    return render(request, 'crud_app/home.html')

@login_required
def product_list(request):
    products = Product.objects.all()
    return render(request, 'crud_app/product_list.html', {'products': products})

@login_required
def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product created successfully!')
            return redirect('crud_app:product_list')
    else:
        form = ProductForm()
    return render(request, 'crud_app/product_form.html', {'form': form})

@login_required
def product_update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product updated successfully!')
            return redirect('crud_app:product_list')
    else:
        form = ProductForm(instance=product)
    return render(request, 'crud_app/product_form.html', {'form': form})

@login_required
def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        messages.success(request, 'Product deleted successfully!')
        return redirect('crud_app:product_list')
    return render(request, 'crud_app/product_confirm_delete.html', {'product': product})



# Supplier CRUD Views
@login_required
def supplier_list(request):
    suppliers = Supplier.objects.all()
    return render(request, 'crud_app/supplier_list.html', {'suppliers': suppliers})

@login_required
def supplier_create(request):
    if request.method == 'POST':
        form = SupplierForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('crud_app:supplier_list')
    else:
        form = SupplierForm()
    return render(request, 'crud_app/supplier_form.html', {'form': form})

@login_required
def supplier_update(request, pk):
    supplier = get_object_or_404(Supplier, pk=pk)
    if request.method == 'POST':
        form = SupplierForm(request.POST, instance=supplier)
        if form.is_valid():
            form.save()
            return redirect('crud_app:supplier_list')
    else:
        form = SupplierForm(instance=supplier)
    return render(request, 'crud_app/supplier_form.html', {'form': form})

@login_required
def supplier_delete(request, pk):
    supplier = get_object_or_404(Supplier, pk=pk)
    if request.method == 'POST':
        supplier.delete()
        return redirect('crud_app:supplier_list')
    return render(request, 'crud_app/supplier_confirm_delete.html', {'supplier': supplier})