from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from store.models import Product as Product
import time


class TestSeleniumProducts(StaticLiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        PATH_WEBDRIVER = r'C:\Users\USER\Documents\ChromeDriver\chromedriver.exe'
        service = Service(PATH_WEBDRIVER)
        cls.driver = webdriver.Chrome(service=service)
        cls.driver.set_window_size(1600, 1000)
        n = 10
        for id in range(n):
            Product.objects.create(
                name='Producto ' + str(id),
                description='descripcion del producto ' + str(id),
                price='500',
                stock=17
            )

    def test_title(self):
        browser = self.driver
        url = self.live_server_url
        browser.get(url + '/')
        time.sleep(1)
        self.assertIn('Webstore', browser.title)

    def test_cart(self):
        browser = self.driver
        url = self.live_server_url
        browser.get(url + '/store/')
        time.sleep(2)
        btn_add_cart = browser.find_element(By.LINK_TEXT, 'Agregar')
        time.sleep(2)
        btn_add_cart.click()
        time.sleep(2)
        btn_badge = browser.find_element(By.ID, 'cart-badge')
        time.sleep(2)
        btn_badge.click()
        time.sleep(2)
        total = browser.find_element(By.ID, 'Total')
        self.assertIn('Total = $500.00', total.text)
