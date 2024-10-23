from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Auction_listings(models.Model):
    title=models.CharField(max_length=64)
    Owner=models.ForeignKey(User, on_delete=models.CASCADE , related_name="seller")
    description=models.CharField(max_length=350)
    imgurl=models.CharField(max_length=99999)
    startingbid = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='cars')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title
    
    
class Bids(models.Model):
    pass

class Comments(models.Model):
    pass