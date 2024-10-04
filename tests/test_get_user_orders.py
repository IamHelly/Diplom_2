from urls import Urls
from data_users import DataUser
import requests
import allure


class TestsGetUserOrders:
    @allure.title('Проверка получения заказов авторизованного пользователя')
    def test_get_user_orders_with_login(self):
        response_login = requests.post(f"{Urls.BASE_URL}/api/auth/login", data={
            "email": DataUser.EMAIL,
            "password": DataUser.PASSWORD
        })
        token = response_login.json()["accessToken"]
        response_get_orders = requests.get(f"{Urls.BASE_URL}/api/orders", headers={'Authorization': token})
        check_success_get_orders = response_get_orders.json()["success"]
        assert response_get_orders.status_code == 200 and check_success_get_orders is True

    @allure.title('Проверка невозможности получения заказов неавторизованного пользователя')
    def test_get_user_orders_without_authorization(self):
        response_get_orders = requests.get(f"{Urls.BASE_URL}/api/orders")
        message_response_get_orders = response_get_orders.json()["message"]
        assert response_get_orders.status_code == 401 and message_response_get_orders == 'You should be authorised'
