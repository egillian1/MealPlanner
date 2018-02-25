from django.db import models

class Recipe(models.Model):
    recipe_name = models.CharField(max_length=300)
    recipe_url = models.CharField(max_length=400)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.recipe_name
