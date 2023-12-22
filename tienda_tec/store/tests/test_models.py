from django.test import TestCase
from store.models import Product


class TestProductModel(TestCase):
    @classmethod
    def setUpTestData(self):
        p = Product(name="Prueba 1",
                    description="Es una prueba",
                    price='550')
        p.save()
        self.products = Product.objects.all()

    def test_save(self):
        self.assertEquals(len(self.products), 1)
        self.assertIs(len(self.products) > 0, True)
        self.assertEquals(self.products[0].sub_title, 'Subtitulo 1')

    def test_product_cost(self):
        self.assertEquals(self.products[0].cost, 550)
