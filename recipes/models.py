from django.db import models

class Recipe(models.Model):
    CATEGORY_CHOICES = [
        ('Dessert', 'Dessert'),
        ('Breakfast', 'Breakfast'),
        ('Lunch', 'Lunch'),
        ('Dinner', 'Dinner'),
    ]

    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='recipes/images/', blank=True, null=True)
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES)  # Use choices here
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
