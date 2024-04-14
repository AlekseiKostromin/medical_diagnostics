from django.db import models

from main.models import LabTest
from users.models import User


class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='покупатель')
    labtests = models.ManyToManyField(LabTest, through='CartItem', verbose_name='анализы', blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='создана')

    def __str__(self):
        return f"Cart for {self.user}"

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, verbose_name='корзина')
    labtest = models.ForeignKey(LabTest, on_delete=models.CASCADE, verbose_name='анализ')
    quantity = models.PositiveIntegerField(default=1, verbose_name='кол-во')
    price = models.PositiveIntegerField(verbose_name='цена', null=True, blank=True)
    total = models.PositiveIntegerField(verbose_name='итого', null=True, blank=True)

    def __str__(self):
        return f"{self.quantity} x {self.labtest.name}"

    class Meta:
        verbose_name = 'Товары в корзине'
        verbose_name_plural = 'Товары в корзине'
