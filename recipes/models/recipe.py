# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.urlresolvers import reverse
from django.db import models
from django.contrib.auth.models import User


class RecipeTypes(object):
    UNKNOWN = '10'
    ENTREE = '30'
    SOUP = '40'
    SALAD = '50'
    DRINK = '60'
    DESSERT = '70'
    SIDE_DISH = '80'
    SAUCE_DRESSING = '90'
    SEASONING = '100'


class Recipe(models.Model):
    title = models.CharField(max_length=100, help_text="The descriptive title for this recipe")

    RECIPE_TYPE_CHOICES = (
        (RecipeTypes.UNKNOWN, "Unknown"),
        (RecipeTypes.ENTREE, "Entree"),
        (RecipeTypes.SOUP, "Soup"),
        (RecipeTypes.SALAD, "Salad"),
        (RecipeTypes.DRINK, "Drink"),
        (RecipeTypes.DESSERT, "Dessert"),
        (RecipeTypes.SIDE_DISH, "Side Dish"),
        (RecipeTypes.SAUCE_DRESSING, "Sauce/Dressing"),
        (RecipeTypes.SEASONING, "Seasoning"),
    )
    recipe_type = models.CharField(max_length=20, choices=RECIPE_TYPE_CHOICES, default='Unknown',
                                   help_text="The category for this recipe")

    creator = models.ForeignKey(User, help_text="The user who created this recipe instance", null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('planner:recipes-detail', kwargs={'pk': self.id})
