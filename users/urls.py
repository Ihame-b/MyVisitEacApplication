from atexit import register
from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_view

urlpatterns = [
 path('', views.home, name='home'),
 path('register/', views.register, name='register'),
 path('profile/', views.profile, name='profile'),
 path('aboutuslab/', views.aboutuslab, name='aboutuslab'),
 path('feedback/', views.feedback, name='feedback'),
 path('adminpage/', views.admin, name='adminpage'),
 path('Tusers/', views.usersTble, name='Tusers'),
 path('Tpro/', views.productTble, name='Tpro'),
 path('login/', auth_view.LoginView.as_view(template_name='users/login.html'), name='login'),
 path('logout/', auth_view.LogoutView.as_view(template_name='users/logout.html'), name='logout'),

#aimable
path('maindash/', views.basedash, name='maindash'),
path('dash/', views.dash, name='dash'),
path('request/', views.request, name='request'),
path('stock/', views.stock, name='stock'),

path('polls/', views.index, name='polls'),
path('delete/<int:id>', views.userdelete, name='delete'),
path('deletep/<int:id>', views.prodelete, name='deletep'),
# path('update/<int:id>', views.userupdate, name='update')

]