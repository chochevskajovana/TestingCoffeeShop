import time

from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By


class Login:
    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        username_input = self.driver.find_element(By.NAME, "username")
        password_input = self.driver.find_element(By.NAME, "password")
        login_button = self.driver.find_element(By.ID, "login_button")

        username_input.send_keys(username)
        password_input.send_keys(password)
        login_button.click()


class Products:
    def __init__(self, driver):
        self.driver = driver

    def click_products_nav_button(self):
        products_button = self.driver.find_element(By.ID, "products_nav_btn")
        products_button.click()
        time.sleep(2)

    def select_product_and_add_to_cart(self, product):
        products = self.driver.find_elements(By.CLASS_NAME, "product-card")
        if len(products) > 0:
            add_to_cart_button = products[product].find_element(By.ID, "add_to_cart")
            add_to_cart_button.click()
        time.sleep(2)

        assert "Your cart is empty" not in self.driver.page_source


class Cart:
    def __init__(self, driver):
        self.driver = driver

    def check_empty_cart(self):
        cart_button = self.driver.find_element(By.ID, "cart_nav_btn")
        cart_button.click()
        time.sleep(2)
        assert "Your cart is empty" in self.driver.page_source


class BuyCoffeeTests(LiveServerTestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://127.0.0.1:8000/login")
        time.sleep(2)
        self.login_page = Login(self.driver)
        self.products_page = Products(self.driver)
        self.cart_page = Cart(self.driver)
        self.login_user()

    def login_user(self):
        self.login_page.login("admin", "201107superuser")
        time.sleep(2)
        assert "Logout" in self.driver.page_source

    def test_buying_coffee(self):
        self.cart_page.check_empty_cart()
        self.products_page.click_products_nav_button()
        self.products_page.select_product_and_add_to_cart(0)
