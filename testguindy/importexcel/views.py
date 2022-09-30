from django.shortcuts import render
from django.http import HttpResponse
from .resources import CategoriesResource
from tablib import Dataset
from .models import Categories

# Create your views here.
def simple_upload(request):
    if request.method == 'POST':
        categories_resource = CategoriesResource()
        dataset = Dataset()
        new_categories = request.FILES['myfile']

        imported_data = dataset.load(new_categories.read(),format='xlsx')
        #print(imported_data)
        for data in imported_data:
                print(data[1])
                value = Categories(
                    data[0],
                    data[1],
                    data[2],
                    data[3]
                    )
                value.save()    
    return render(request, 'input.html')    