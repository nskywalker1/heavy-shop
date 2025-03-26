from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=35,
                            unique=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        indexes = [models.Index(fields=['name'])]
        verbose_name = 'category'
        verbose_name_plural = 'categories'


class Product(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    category = models.ForeignKey(Category,
                                 related_name='products',
                                 on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products/%Y/%m/%d',
                              blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10,
                                decimal_places=2)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    discount = models.DecimalField(max_digits=4,
                                   default=0.00,
                                   decimal_places=2)

    class Meta:
        ordering = ['name']
        indexes = [models.Index(fields=['id', 'slug']),
                   models.Index(fields=['name']),
                   models.Index(fields=['-created'])
                   ]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('main:product-detail',
                       args={'slug': self.slug})

    def sell_price(self):
        if self.discount:
            return round(self.price - self.price * self.discount / 100, 2)
        return self.price
