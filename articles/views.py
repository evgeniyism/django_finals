from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from .models import Item, Articles, Cart, CartItem, Order, OrderItem
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.contrib.auth import logout, login
from .constants import USER_NOT_FOUND, CART_IS_EMPTY, CART
from django.db.models import F


def index(request):
    template = 'shop/index.html'
    items_list = Item.objects.all()
    articles_list = Articles.objects.all().order_by('date')
    context = {'items_list': items_list,
               'articles_list': articles_list}
    return render(request, template, context=context)


def empty_section(request):
    return render(request, 'shop/empty_section.html')


def item_page(request):
    template = 'shop/item-page.html'
    item = Item.objects.get(id=request.GET['id'][0])
    context = {'item': item}
    return render(request, template, context=context)


def category(request):
    template = 'shop/category.html'
    current_category = request.GET['category']
    items_list = Paginator(Item.objects.filter(type__short_name__contains=current_category), 1)
    page_number = request.GET.get('page')
    page_obj = items_list.get_page(page_number)
    category_name = Item.objects.filter(type__short_name__contains=current_category)[0].type.title
    context = {'items_list': items_list,
               'category_name': category_name,
               'page_obj': page_obj,
               'current_category': current_category}
    return render(request, template, context=context)


def login_view(request):
    if request.method == 'GET':
        return render(request, 'shop/login.html')

    if request.method == 'POST':
        try:
            user = User.objects.get(username=request.POST['username'])
            user = authenticate(username=user.username, password=request.POST['password'])
            if user is None:
                raise Exception(USER_NOT_FOUND)
            login(request, user)
            return redirect('home')
        except Exception:
            context = {'status': USER_NOT_FOUND}
            return render(request, 'shop/login.html', context=context)


def registration(request):
    if request.method == 'GET':
        return render(request, 'shop/registration.html')

    if request.method == 'POST':
        User.objects.create_user(request.POST['email'], request.POST['email'], request.POST['password'])
        return redirect('login')


def logout_view(request):
    logout(request)
    return redirect('home')


def button(request):
    return render(request, 'shop/button.html')


def add_to_cart(request):
    if request.method == 'POST':
        user = User.objects.get(id=request.session['_auth_user_id'][0])
        try:
            cart, created_cart = Cart.objects.get_or_create(user=user)
            product = Item.objects.get(id=request.POST['item'])
            cart_item, created_cartitem = CartItem.objects.get_or_create(cart=cart, item=product)
            cart_item.quantity = F('quantity') + 1
            cart_item.save()
        except Exception:
            raise KeyError

    redirect_url = request.POST['current']
    return redirect(redirect_url)


def show_cart(request):
    user = User.objects.get(id=request.session['_auth_user_id'])
    try:
        cart = Cart.objects.get(user=user)
        purchase = CartItem.objects.filter(cart=cart)
        products_count = len(purchase)
        context = {
            'purchase': purchase,
            'products_count': products_count,
            'message': CART
        }
        return render(request, 'shop/cart.html', context=context)
    except:
        context = {
            'message': CART_IS_EMPTY,
        }
        return render(request, 'shop/cart.html', context=context)


def checkout(request):
    user = User.objects.get(id=request.session['_auth_user_id'])
    cart = Cart.objects.get(user=user)
    order = Order.objects.create(user=cart.user)
    cart_items = CartItem.objects.filter(cart=cart)
    for item in cart_items:
        OrderItem.objects.create(item=item.item, quantity=item.quantity, order=order)
    Cart.objects.get(user=user).delete()
    return redirect('cart')
