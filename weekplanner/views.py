from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse

from pprint import pprint
import logging
logger = logging.getLogger("docker.console")

from .models import Recipe

def index(request):
    latest_recipe_list = Recipe.objects.order_by('-pub_date')[:5]
    #template = loader.get_template('recipes/index.html')
    context = {
        'latest_recipe_list': latest_recipe_list,
    }
    return render(request, 'recipes/index.html', context)
    #return HttpResponse(template.render(context, request))
    #return HttpResponse("Hello, world. You're at the weekly planner index.")

def detail(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    logger.info("Details")
    return render(request, 'recipes/detail.html', {'recipe': recipe})

def addRecipe(request):
    logger.info("Adding recipe")
    return HttpResponse("You're adding a recipe")

def edit(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    logger.info("Editing recipe")
    logger.info(recipe)
    post = request.POST
    recipe.recipe_name = post['name']
    recipe.recipe_url = post['url']
    recipe.save()
    return HttpResponseRedirect(reverse('weekplanner:index'))
