from rest_framework.test import APITestCase
import json
from store.models import Product


class BasicTest(APITestCase):
    def setUp(self):
        self.url = '/api/'

    def test_get(self):
        response = self.client.get(self.url, format='json')
        self.assertEquals(response.status_code, 200)


class TestProductModel(APITestCase):
    def setUp(self):
        self.url = '/apiProducts/'

    @classmethod
    def setUpTestData(self):
        p = Product(name="Prueba 1",
                    description="Es una prueba",
                    price='550')
        p.save()
        self.products = Product.objects.all()

    def test_with_out_parameters(self):
        data = {
            'parameters': {}
        }

        response = self.client.post(self.url, data=data, format='json')
        self.assertEquals(response.status_code, 200)
        data_res = json.loads(response.data['Resultado'])
        self.assertEquals(len(data_res), 1)
        self.assertEquals(data_res[0]['name'], "Prueba 1")
