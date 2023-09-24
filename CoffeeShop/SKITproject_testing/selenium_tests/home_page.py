import time

from django.test import LiveServerTestCase
from selenium import webdriver


class HomePageTest(LiveServerTestCase):

    def test_home_page(self):
        driver = webdriver.Chrome()
        time.sleep(2)
        driver.get('http://127.0.0.1:8000/home')
        time.sleep(2)
        assert "Coffee Shop" in driver.title

    def test_default_page(self):
        driver = webdriver.Chrome()
        time.sleep(2)
        driver.get('http://127.0.0.1:8000/')
        time.sleep(2)
        assert "Coffee Shop" in driver.title
