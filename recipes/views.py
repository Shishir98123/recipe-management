from django.shortcuts import render, redirect, get_object_or_404
from .models import Recipe
from .forms import RecipeForm

# Create your views here.

def recipe_list(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipes/recipe_list.html', {'recipes': recipes})

def recipe_add(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('recipe_list')
        else:
         form = RecipeForm()
         return render (request, 'recipes/recipe_form.html', {'form': form})
      
def recipe_edit(request, pk):
   recipe = get_object_or_404(Recipe, pk=pk)
   if request.method == 'POST':
      form = RecipeForm(request.POST, request.FILES, instance=recipe)
      return redirect('recipe_list')
   else:
      form = RecipeForm(instance=recipe)
      return render(request, 'recipes/recipe_form.html', {'form': form})
   
def recipe_delete(request, pk):
   recipe = get_object_or_404(Recipe, pk=pk)
   recipe.delete()
   return redirect('recipe_list')