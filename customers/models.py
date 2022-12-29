from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=100)
    industry = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Order(models.Model):
    customer = models.ForeignKey(
        Customer, related_name="orders", on_delete=models.CASCADE)
    description = models.CharField(max_length=250)
    totalInCents = models.IntegerField()

    def __str__(self):
        return self.description
