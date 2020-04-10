from django.db import models
from django.db.models.signals import pre_save, post_save
from .utils import unique_slug_generator
from django.urls import reverse


class ProductManager(models.Model):
    def get_by_id(self, id):
        qs = self.get_queryset().filter(id=id)
        if qs.count() == 1:
            return qs.first()
        return None


class Product(models.Model):
    ASSAULT = 'ASSAULT'
    SNIPER = 'SNIPER'
    SMG = 'SMG'
    LMG = 'LMG'
    SHOTGUN = 'SHOTGUN'
    HANDGUN = 'HANDGUN'
    EMPTY = '------'
    type_choices = [
        (ASSAULT, 'Assault'),
        (SNIPER, 'Sniper'),
        (SMG, 'SMG'),
        (LMG, 'LMG'),
        (SHOTGUN, 'Shot gun'),
        (HANDGUN, 'Hand gun')
    ]
    title = models.CharField(max_length=100)
    slug = models.SlugField(blank=True, unique=True)
    price = models.DecimalField(decimal_places=2, max_digits=20)
    image = models.ImageField(upload_to='products/')
    description = models.TextField(max_length=2000)
    type = models.CharField(
        max_length=15,
        choices=type_choices
    )

    def get_absolute_url(self):
        return reverse("detail", kwargs={"slug": self.slug})

    def __str__(self):
        return self.title


def product_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(product_pre_save_receiver, sender=Product)
