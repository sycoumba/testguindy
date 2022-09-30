from import_export import resources
from .models import Categories

class CategoriesResource(resources.ModelResource):
    class Meta:
        model = Categories