from django.contrib.auth.decorators import login_required
from django.shortcuts import render,get_object_or_404,redirect
from .models import Category,Product
from .forms import NewProductForm,EditProductForm
from django.db.models import Q
from django.contrib import messages
from django.core.paginator import Paginator
import os


def products(request):
    query = request.GET.get('query', '')
    category_id = request.GET.get('category_id', 0)
    categories = Category.objects.all()
    products = Product.objects.filter(is_sold=False)
    if category_id:
        products = products.filter(category_id=category_id)
       
    if query:
        products = products.filter(Q(name__icontains=query) | Q(description__icontains=query))
       
    return render(request, 'product/index.html', {
        'products': products,
        'query': query,
        'categories': categories,
        'category_id': int(category_id),
        
    })

def detail(request,pk):
    product=get_object_or_404(Product,pk=pk)
    return render(request, 'product/detail.html', {
        'product': product,})
@login_required  
def myproducts(request):
    query = request.GET.get('query', '')
    category_id = request.GET.get('category', 0)
    categories = Category.objects.all()
    products = Product.objects.filter(is_sold=False,created_by=request.user)
    if category_id:
        products = products.filter(category_id=category_id)
       
    if query:
        products = products.filter(Q(name__icontains=query) | Q(description__icontains=query))
     
    return render(request, 'product/index.html', {
        'products': products,
        'query': query,
        'categories': categories,
        'category_id': int(category_id),
        
    })

@login_required    
def create(request):
    if request.method == 'POST':
        form = NewProductForm(request.POST, request.FILES)

        if form.is_valid():
            product = form.save(commit=False)
            product.created_by = request.user
            product.save()
            messages.success(request,"Product has been created successfully!")
            return redirect("/")
    else:
        form = NewProductForm()

    return render(request, 'product/create.html', {
        'form': form,
        'title': 'Create Product',
    })
    
    
@login_required    
def edit(request,pk):
    product=get_object_or_404(Product,pk=pk,created_by=request.user)
    if request.method == 'POST':
        form = EditProductForm(request.POST, request.FILES,instance=product)
        if form.is_valid():
            form.save()
            messages.success(request,"Product has been edited successfully!")
            return redirect('/')
    else:
        form = EditProductForm(instance=product)

    return render(request, 'product/edit.html', {
        'form': form,
        'title': 'Edit product',
    })
@login_required
def delete(request,pk):
    product=get_object_or_404(Product,pk=pk,created_by=request.user)
    product.delete()
    os.remove(product.image.path)
    messages.success(request,"Product has been deleted successfully!")
    return redirect("/")    
    