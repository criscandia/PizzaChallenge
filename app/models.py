from django.db import models

class Pizza(models.Model):
    FLAVOR_CHOICES = [
        ('MARG', 'Margarita'),
        ('PEPP', 'Pepperoni'),
        ('HAWA', 'Hawaiana'),
    ]
    name = models.CharField(max_length=100)
    flavor = models.CharField(max_length=10, choices=FLAVOR_CHOICES)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Client(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    email = models.EmailField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.client.name} ordered a {self.pizza.name} on {self.date_added.strftime('%Y-%m-%d')}"
