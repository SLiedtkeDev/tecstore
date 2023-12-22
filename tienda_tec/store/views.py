from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView
from .models import Product
from .forms import OrderForm
import json


class ProductListView(ListView):
    template_name = 'store/product_list.html'
    model = Product


def success_order(request):
    if request.method == 'POST':
        order = request.session['order']
        for product in order:
            prod_id = product['id']
            quantity = product['quantity']
            prod = Product.objects.get(pk=prod_id)
            prod.stock = prod.stock - quantity
            prod.save()


class CreateOrder(CreateView):
    form_class = OrderForm
    template_name = 'store/order_client.html'
    success_url = reverse_lazy('core:home')

    def form_valid(self, form):
        order = self.request.session['order']
        for pro in order:
            id = pro['id']
            qty = pro['quantity']
            p = Product.objects.get(pk=id)
            p.stock = p.stock - qty
            p.save()
        order = form.save()
        return super().form_valid(form)

    def get_form_kwargs(self):
        kwargs = super(CreateOrder, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs


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
            dict_product['producto'] = product.name
            dict_product['quantity'] = qty
            dict_product['price'] = product.price
            dict_product['sub_total'] = product.price * qty
            total += dict_product['sub_total']
            order.append(dict_product)
        # Se colocan en sesión estos datos
        request.session['total'] = total
        request.session['order'] = order
        return render(request, 'store/detail_order.html', {'order': order, 'total': total})
    else:
        return render(request, 'store/detail_order.html')
