from locust import HttpUser, between, task


class CoffeeShopUser(HttpUser):
    wait_time = between(1, 3)

    @task
    def view_home_page(self):
        self.client.get("/home")

    @task
    def view_home_page_2(self):
        self.client.get("")

    @task
    def view_coffees_page(self):
        self.client.get(url="/products")

    @task
    def search_coffees_page(self):
        self.client.get("/search_feature")

    @task
    def view_cart_page(self):
        self.client.get("/cart")

    @task
    def empty_cart_page(self):
        self.client.get("/cart_empty")

    @task
    def view_orders_page(self):
        self.client.get("/orders")

    @task
    def login_page(self):
        data = {
            "username": "admin",
            "password": "201107superuser"
        }
        self.client.post("/login/", data=data)

    @task
    def register_page(self):
        data = {
            "username": "testTest",
            "email": "test@test.com",
            "password1": "Test12#",
            "password2": "Test12#"
        }
        self.client.post("/register/", data=data)

    @task
    def logout_page(self):
        self.client.get("/logout")

    @task
    def not_allowed_page(self):
        self.client.get("/not_allowed")
