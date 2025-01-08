from django.db import models

# Create your models here.
class Recipe(models.Model):
   name = models.CharField(max_length=100)
   description = models.TextField()
   image= models.ImageField(upload_to='recipes/images/', blank=True, null=True)
   category = models.CharField(max_length=100)
   choices = [('Dessert', 'Dessert'), ('Breakfast', 'Breakfast'), ('Lunch', 'Lunch'), ('Dinner', 'Dinner')]
   
   created_at = models.DateTimeField(auto_now_add=True)
   
   def __str__(self):
       return self.name