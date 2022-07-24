from django.urls import path

from recipes.views import (
    RecipeCreateView,
    RecipeUpdateView,
    log_rating,
    RecipeDetailView,
    RecipelistView,
)

urlpatterns = [
    path("", RecipelistView.as_view(), name="recipes_list"),
    path("<int:pk>/", RecipeDetailView.as_view(), name="recipe_detail"),
    path("new/", RecipeCreateView.as_view(), name="recipe_new"),
    path("<int:pk>/edit/", RecipeUpdateView.as_view(), name="recipe_edit"),
    path("<int:recipe_id>/ratings/", log_rating, name="recipe_rating"),
]
