from django.contrib.auth import views as auth_views
from django.urls import path
from .forms import LoginForm
from . import views
# from .forms import LoginForm

app_name = 'core'
urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'), 
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html', authentication_form=LoginForm), name='login'),
    path('logout/', views.log_out, name='log_out'),   
    path('accounts/profile/', views.profile, name='profile'), 
    path('manage/users/', views.manage_users, name='manage_users'),
    path('<int:pk>/delete_user/', views.delete_user, name='delete_user'),
]
