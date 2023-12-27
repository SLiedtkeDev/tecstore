from django.test import TestCase
from store.models import Product


class TestProductModel(TestCase):
    @classmethod
    def setUpTestData(self):
        p = Product(name="Prueba 1",
                    description="Es una prueba",
                    stock=1,
                    price='550')
        p.save()
        self.products = Product.objects.all()

    def test_save(self):
        self.assertEquals(len(self.products), 1)
        self.assertIs(len(self.products) > 0, True)
        self.assertEquals(self.products[0].description, 'Es una prueba')

    def test_product_cost(self):
        self.assertEquals(self.products[0].price, 550)
