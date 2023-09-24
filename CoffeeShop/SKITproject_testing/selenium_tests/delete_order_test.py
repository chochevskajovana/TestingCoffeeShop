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


class Orders:
    def __init__(self, driver):
        self.driver = driver

    def click_orders_nav_button(self):
        orders_button = self.driver.find_element(By.ID, "orders_nav_btn")
        orders_button.click()
        time.sleep(2)

    def select_order_for_delete(self):
        orders = self.driver.find_elements(By.CLASS_NAME, "order-card")
        if len(orders) > 0:
            delete_button = orders[len(orders) - 1].find_element(By.CLASS_NAME, "delete_order_btn")
            self.driver.execute_script("arguments[0].scrollIntoView();", delete_button)
            delete_button.click()
        time.sleep(2)


class DeleteOrderTests(LiveServerTestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://127.0.0.1:8000/login")
        time.sleep(2)
        self.login_page = Login(self.driver)
        self.orders_page = Orders(self.driver)
        self.login_user()

    def login_user(self):
        self.login_page.login("admin", "201107superuser")
        time.sleep(2)
        assert "Logout" in self.driver.page_source

    def test_delete_order_coffee(self):
        self.orders_page.click_orders_nav_button()
        self.orders_page.select_order_for_delete()
