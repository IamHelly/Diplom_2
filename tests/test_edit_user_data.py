from urls import Urls
from data_users import DataUniqueUser
import requests
import allure


class TestsEditUserData:
    @allure.title('Проверка изменения email с авторизацией')
    def test_edit_email_with_login_user(self):
        # Шаг 1 - регистрация пользователя
        payload = {
            "email": DataUniqueUser.EMAIL,
            "password": DataUniqueUser.PASSWORD,
            "name": DataUniqueUser.NAME
        }
        requests.post(f"{Urls.BASE_URL}/api/auth/register", data=payload)
        # Шаг 2 - логин нового пользователя и получение тела ответа
        response_login = requests.post(f"{Urls.BASE_URL}/api/auth/login", data={
            "email": DataUniqueUser.EMAIL,
            "password": DataUniqueUser.PASSWORD
        })
        token = response_login.json()["accessToken"]
        # Шаг 3 - изменение данных пользователя
        new_email = 'amelystar@yandex.ru'
        requests.patch(f"{Urls.BASE_URL}/api/auth/user", data={"email": new_email}, headers={'Authorization': token})
        response_user = requests.get(f"{Urls.BASE_URL}/api/auth/user", headers={'Authorization': token})
        current_email = response_user.json()['user']['email']
        assert current_email == new_email
        # Шаг 4 - удаление тестового пользователя
        requests.delete(f"{Urls.BASE_URL}/api/auth/user", headers={'Authorization': token})

    @allure.title('Проверка изменения name с авторизацией')
    def test_edit_name_with_login_user(self):
        # Шаг 1 - регистрация пользователя
        payload = {
            "email": DataUniqueUser.EMAIL,
            "password": DataUniqueUser.PASSWORD,
            "name": DataUniqueUser.NAME
        }
        requests.post(f"{Urls.BASE_URL}/api/auth/register", data=payload)
        # Шаг 2 - логин нового пользователя и получение тела ответа
        response_login = requests.post(f"{Urls.BASE_URL}/api/auth/login", data={
            "email": DataUniqueUser.EMAIL,
            "password": DataUniqueUser.PASSWORD
        })
        token = response_login.json()["accessToken"]
        # Шаг 3 - изменение данных пользователя
        new_name = 'Амелия'
        requests.patch(f"{Urls.BASE_URL}/api/auth/user", data={"name": new_name}, headers={'Authorization': token})
        response_user = requests.get(f"{Urls.BASE_URL}/api/auth/user", headers={'Authorization': token})
        current_name = response_user.json()['user']['name']
        assert current_name == new_name
        # Шаг 4 - удаление тестового пользователя
        requests.delete(f"{Urls.BASE_URL}/api/auth/user", headers={'Authorization': token})

    @allure.title('Проверка невозможности изменения email без авторизации')
    def test_edit_email_without_authorization(self):
        new_email = 'amelystar@yandex.ru'
        response_user = requests.patch(f"{Urls.BASE_URL}/api/auth/user", data={"email": new_email})
        message = response_user.json()["message"]
        assert response_user.status_code == 401 and message == 'You should be authorised'

    @allure.title('Проверка невозможности изменения name без авторизации')
    def test_edit_name_without_authorization(self):
        new_name = 'Амелия'
        response_user = requests.patch(f"{Urls.BASE_URL}/api/auth/user", data={"name": new_name})
        message = response_user.json()["message"]
        assert response_user.status_code == 401 and message == 'You should be authorised'
