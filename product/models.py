from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Brand(models.Model):
    title = models.CharField(
        max_length=123
    )
    description = models.TextField()
    logo = models.ImageField(
        upload_to='media/logo'
    )

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(
        max_length=123
    )

    def __str__(self):
        return self.title


class Color(models.Model):
    title = models.CharField(
        max_length=123
    )

    def __str__(self):
        return self.title


class Image(models.Model):
    file = models.ImageField(
        upload_to='media/product'
    )
    is_main = models.BooleanField(
        default=False
    )


class Product(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.PROTECT
    )
    title = models.CharField(
        max_length=123
    )
    brands = models.ManyToManyField(
        Brand
    )
    color = models.ForeignKey(
        Color,
        models.PROTECT
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT
    )
    images = models.ManyToManyField(
        Image
    )
    description = models.TextField()
    size = models.PositiveSmallIntegerField(
        choices=(
            (1, 'XS'),
            (2, 'S'),
            (3, 'M'),
            (4, 'L'),
            (5, 'XL'),
            (6, 'XXL'),
        )
    )
    price = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0.00
    )
    discount = models.PositiveIntegerField(
        blank=True,
        null=True
    )
    created_date = models.DateTimeField(
        auto_now_add=True
    )
    update_date = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return self.title


class Storage(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.PROTECT
    )
    quantity = models.PositiveIntegerField()
    status = models.PositiveSmallIntegerField(
        choices=(
            (1, 'Нет в наличии'),
            (2, 'Скоро в наличии'),
            (3, 'Есть в наличии'),
        )
    )
    created_date = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return str(self.product)
