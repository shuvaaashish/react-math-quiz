from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class auction_listings(models.Model):
    pass

class bids(models.Model):
    pass

class comments(models.Model):
    pass