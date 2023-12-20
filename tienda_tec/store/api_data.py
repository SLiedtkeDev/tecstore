import json
from .models import Product


class Data:

    # parameter es de tipo Json
    def get_products(self, parameters=None):
        projects = Product.objects.all()
        if parameters:
            if 'id' in parameters:
                # projects = projects.filter(title = parameters['title'])
                projects = projects.filter(title=parameters['id'])
            if 'name' in parameters:
                projects = projects.filter(
                    description__contains=parameters['name'])
        return projects
