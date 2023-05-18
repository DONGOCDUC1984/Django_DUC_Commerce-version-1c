from django.urls import path
from . import views
app_name="product"
urlpatterns = [
    path('', views.products, name='products'),
    path("create/",views.create,name="create"),
    path("<int:pk>/",views.detail,name="detail"),
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('<int:pk>/edit/', views.edit, name='edit'),
    path("myproducts/",views.myproducts,name="myproducts"),
   
]