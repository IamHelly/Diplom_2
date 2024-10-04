from urls import Urls
from data_users import DataUser
import requests
import allure


class TestsCreateOrder:
    @allure.title('Проверка создания заказа с авторизацией и ингредиентами')
    def test_create_order_with_login_and_with_ingredients(self):
        response_login = requests.post(f"{Urls.BASE_URL}/api/auth/login", data={
            "email": DataUser.EMAIL,
            "password": DataUser.PASSWORD
        })
        token = response_login.json()["accessToken"]
        response_orders = requests.post(f"{Urls.BASE_URL}/api/orders", json={
            "ingredients": ["61c0c5a71d1f82001bdaaa6c", "61c0c5a71d1f82001bdaaa6e", "61c0c5a71d1f82001bdaaa76", "61c0c5a71d1f82001bdaaa7a"]
        }, headers={'Authorization': token})
        check_success_create_order = response_orders.json()["success"]
        assert response_orders.status_code == 200 and check_success_create_order is True

    @allure.title('Проверка создания заказа без авторизации и с одним ингредиентом')
    def test_create_order_without_authorization_and_with_single_ingredients(self):
        response_orders = requests.post(f"{Urls.BASE_URL}/api/orders", json={
            "ingredients": ["61c0c5a71d1f82001bdaaa77"]
        })
        check_success_create_order = response_orders.json()["success"]
        assert response_orders.status_code == 200 and check_success_create_order is True

    @allure.title('Проверка невозможности создания заказа без ингредиентов')
    def test_not_create_order_with_login_and_without_ingredients(self):
        response_login = requests.post(f"{Urls.BASE_URL}/api/auth/login", data={
            "email": DataUser.EMAIL,
            "password": DataUser.PASSWORD
        })
        token = response_login.json()["accessToken"]
        response_orders = requests.post(f"{Urls.BASE_URL}/api/orders", json={"ingredients": []}, headers={'Authorization': token})
        message_response_create_order = response_orders.json()["message"]
        assert response_orders.status_code == 400 and message_response_create_order == 'Ingredient ids must be provided'

    @allure.title('Проверка невозможности создания заказа с неверным хешем ингредиентов')
    def test_not_create_order_with_invalid_hash_ingredients(self):
        response_orders = requests.post(f"{Urls.BASE_URL}/api/orders", json={
            "ingredients": ["001bdaaa76", "001bdaaa7a"]
        })
        assert response_orders.status_code == 500

    @allure.title('Проверка невозможности создания заказа с наличием одновременно верных и неверных хешей ингредиентов')
    def test_not_create_order_with_correct_and_invalid_hash_ingredients(self):
        response_orders = requests.post(f"{Urls.BASE_URL}/api/orders", json={
            "ingredients": ["61c0c5a71d1f82001bdaaa6c", "61c0c5a71d1f82001bdaaa6e", "001bdaaa76", "001bdaaa7a"]
        })
        assert response_orders.status_code == 500
