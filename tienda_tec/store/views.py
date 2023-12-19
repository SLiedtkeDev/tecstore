from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView
from .models import Product
import json


class ProductListView(ListView):
    template_name = 'store/product_list.html'
    model = Product


def detail_order(request):
    if request.method == 'POST':
        data = request.POST['order_data']
        # Convesión a json
        order_data = json.loads(data)
        total = 0
        order = list()
        for product in order_data.keys():
            qty = order_data[product]
            product = Product.objects.get(pk=int(product))
            dict_product = {}
            dict_product['id'] = product.id
            dict_product['title'] = product.name
            dict_product['quantity'] = qty
            dict_product['price'] = product.price
            dict_product['sub_total'] = service.cost * qty
            total += dict_product['sub_total']
            order.append(dict_product)
        # Se colocan en sesión estos datos
        request.session['total'] = total
        request.session['order'] = order
        return render(request, 'services/detail_order.html', {'order': order, 'total': total})
