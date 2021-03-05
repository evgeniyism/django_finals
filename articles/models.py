from django.db import models
from uuslug import slugify
import datetime
from django.contrib.auth.models import User


# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    short_name = models.CharField(max_length=8, verbose_name='Сокращение')
    description = models.CharField(max_length=255, verbose_name='Описание категории')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория товаров'
        verbose_name_plural = 'Категории товаров'


class Item(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение')
    type = models.ForeignKey('Category', blank=True, on_delete=models.DO_NOTHING)
    slug = models.SlugField(max_length=200, blank=True, default='')
    description = models.CharField(max_length=255, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Item, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class Articles(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    gadget = models.ManyToManyField(Item)
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение')
    text = models.CharField(max_length=255, verbose_name='Текст статьи', blank=True)
    slug = models.SlugField(max_length=200, blank=True, default='')
    date = models.DateField(default=datetime.date.today)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Articles, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Покупатель")
    status_checked = models.BooleanField(default=False, verbose_name="Заказ оплачен")
    products = models.ManyToManyField(Item, through='CartItem', related_name='cart_items')

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'

    def __str__(self):
        return str(self.user)


class CartItem(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, verbose_name="Товар в корзине")
    quantity = models.PositiveSmallIntegerField(verbose_name="Количество", default=0)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.item)


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.RESTRICT, verbose_name="Покупатель")
    products = models.ManyToManyField(Item, through='OrderItem', related_name='order_items')
    date = models.DateField(default=datetime.date.today, verbose_name='Дата заказа')

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'заказы'

    def get_date(self):
        return self.date
    get_date.short_description = 'Дата'
    get_date.admin_order_field = 'date'

    def get_user(self):
        return self.user
    get_user.short_description = 'Покупатель'

    def get_quantity(self):
        items = OrderItem.objects.filter(order=self)
        quantity = len(items)
        return str(quantity)
    get_quantity.short_description = 'Количество товаров'



class OrderItem(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, verbose_name="Товар в заказе")
    quantity = models.PositiveSmallIntegerField(verbose_name="Количество", default=0)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)


    def __str__(self):
        return str(self.item)
