"""shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from articles import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='home'),
    path('index.html', views.index, name='home'),
    path('category.html', views.category, name='category'),
    path('item-page.html', views.item_page, name='item_page'),
    path('cart.html', views.show_cart, name='cart'),
    path('login.html', views.login_view, name='login'),
    path('registration.html', views.registration, name='registration'),
    path('logout.html', views.logout_view, name='logout'),
    path('add_to_cart.html', views.add_to_cart, name='add_to_cart'),
    path('checkout', views.checkout, name='checkout'),
]
