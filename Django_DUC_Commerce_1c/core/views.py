from django.shortcuts import render,redirect,get_object_or_404
from product.models import Category,Product
from .forms import SignupForm
from django.contrib.auth import logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

number_per_page =10

def index(request):
    products=Product.objects.filter(is_sold=False)
    categories=Category.objects.all()
    paginator = Paginator(products, number_per_page)  
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, "core/index.html", 
                  { "products":products,"categories":categories,
                   "page_obj":page_obj,
                   })

def register(request):
    if request.method == "POST":
        form=SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/login") 
        else:
            return render(request, "core/register.html", 
                  {"form":form ,})   
    else:        
        form=SignupForm()
        return render(request, "core/register.html", 
                  {"form":form ,})
@login_required
def profile(request):
   return render(request, 'core/profile.html',) 

@login_required
def manage_users(request):
    if request.user.is_superuser:
        all_users = User.objects.all().values()
        template = loader.get_template('core/all_users.html')
        return HttpResponse(template.render(
            {"all_users": all_users,}, request))
    else:
        return HttpResponse("<h1> Not authorized ! Only for administrator ! </h1>")

@login_required
def delete_user(request,pk):
    if request.user.is_superuser:
        deleted_user=get_object_or_404(User,pk=pk)
        deleted_user.delete()
        messages.success(request,"User has been deleted successfully!")
        return redirect("/manage/users/") 
    else:
        return HttpResponse("<h1> Not authorized ! Only for administrator ! </h1>")
@login_required        
# if I write def logout(request):,in the following line,
# there will be an error 
def log_out(request):
    logout(request)
    return redirect("/")          