import json
from .models import Product


class Data:

    # parameter es de tipo Json
    def get_products(self, parameters=None):
        projects = Product.objects.all()
        if parameters:
            if 'id' in parameters:
                # projects = projects.filter(title = parameters['title'])
                projects = projects.filter(id=parameters['id'])
            if 'name' in parameters:
                projects = projects.filter(
                    name=parameters['name'])
            if 'description' in parameters:
                projects = projects.filter(
                    description__contains=parameters['description'])
            if 'stock' in parameters:
                projects = projects.filter(
                    stock__gt=parameters['stock'])
        return projects
