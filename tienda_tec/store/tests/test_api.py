from django.test import TestCase
from rest_framework.test import APIClient
from django.urls import reverse
from rest_framework import status
from store.models import Product
from store.serializers import ProductSerializer
import json
from rest_framework.test import APITestCase

# PRODUCTS_URL = reverse("store:api")


# def create_product(**params):
#     @classmethod
#     def setUpTestData(self):
#         p = Product(name="Prueba 1",
#                     description="Es una prueba",
#                     stock=1,
#                     price='550')
#         p.save()
#         self.products = Product.objects.all()
#         return self.products


# class ProductApiTest(TestCase):

#     def setUp(self) -> None:
#         self.client = APIClient()

#     def test_retrieve_productd(self):
#         create_product()
#         res = self.client.get(PRODUCTS_URL)
#         products = Product.objects.all()
#         serializer = ProductSerializer(products, many=True)
#         self.assertEquals(res.status_code, status.HTTP_200_OK)
#         self.assertEquals(res.data, serializer.data)


class ProductApi(APITestCase):
    def setUp(self):
        self.url = reverse("store:postapi")
        for i in range(10):
            Product.objects.create(
                name='Proyecto ' + str(i),
                description='description ' + str(i),
                price=i*3,
                stock=12)

    def test_with_out_parameters(self):
        data = {
            'parameters': {}
        }

        response = self.client.post(self.url, data=data, format='json')
        self.assertEquals(response.status_code, 200)
        data_res = json.loads(response.data['Resultado'])
        print(data_res)
        print(len(data_res))
        self.assertEquals(len(data_res), 10)
        self.assertEquals(data_res[0]['name'], "Proyecto 0")

    def test_with_description_parameter(self):
        data = {
            'parameters': {'description': '5'}
        }

        response = self.client.post(self.url, data=data, format='json')
        self.assertEquals(response.status_code, 200)
        data_res = json.loads(response.data['Resultado'])
        self.assertEquals(len(data_res), 1)
        self.assertEquals(data_res[0]['name'], "Proyecto 5")
