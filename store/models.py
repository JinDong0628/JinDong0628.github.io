from django.db import models

# Create your models here.


class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.FloatField(max_digits=6, decimal_places=2)
    inventory = models.IntegerField()
    last_update = models.DataTimeField(auto_now=True)


class Customer(models.Model):
    MEMBERSHIP_Bronze = 'B'
    MEMBERSHIP_Silver = 'S'
    MEMBERSHIP_GOld = 'G'
    MEMBERSHIP_CHOICES = [
        (MEMBERSHIP_Bronze, 'Bronze'),
        (MEMBERSHIP_Silver, 'Silver'),
        (MEMBERSHIP_GOld, 'Gold')
    ]
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=255)
    birth_date = models.DateField(null=True)
    membership = models.CharField(
        max_length=1, choices=MEMBERSHIP_CHOICES, default=MEMBERSHIP_Bronze)


class Order(models.Model):
    PATMENT_STATUS_PENDING = 'P'
    PATMENT_STATUS_COMPLETE = 'C'
    PATMENT_STATUS_FAILED = 'F'
    PATMENT_STATUS_CHOICES = [
        (PATMENT_STATUS_PENDING, 'Pending'),
        (PATMENT_STATUS_COMPLETE, 'Complete'),
        (PATMENT_STATUS_FAILED, 'Failed')
    ]

    placed_at = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(
        max_length=1, choice=PATMENT_STATUS_CHOICES, default=PATMENT_STATUS_PENDING
    )
