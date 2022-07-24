from django.urls import path

from recipes.views import (
    RecipeCreateView,
    change_recipe,
    log_rating,
    RecipeDetailView,
    RecipelistView,
)

urlpatterns = [
    path("", RecipelistView.as_view(), name="recipes_list"),
    path("<int:pk>/", RecipeDetailView.as_view(), name="recipe_detail"),
    path("new/", RecipeCreateView.as_view(), name="recipe_new"),
    path("edit/", change_recipe, name="recipe_edit"),
    path("<int:recipe_id>/ratings/", log_rating, name="recipe_rating"),
]
