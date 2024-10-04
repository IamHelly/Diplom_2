## Дипломный проект. Задание 2: API

### Автотесты для проверки API сервиса Stellar Burgers, где можно собрать и заказать бургер из необычных ингредиентов.

### Реализованные сценарии

Созданы классы тестов для создания, логина, изменения данных пользователя, создания заказа, получения заказов конкретного пользователя.

### Структура проекта

- `tests` - пакет, содержащий тесты для проверки создания, логина, изменения данных пользователя, создания заказа, получения заказов конкретного пользователя;
- `allure_results` - пакет, содержащий Allure-отчет;
- `data_user.py` - файл, содержащий данные для авторизации зарегистрированного пользователя и регистрации нового пользователя;
- `urls.py` - файл, содержащий url запросов.

**Класс TestsRegistrationUser** - содержит тесты для проверки создания пользователя:
1. test_registration_unique_user() - проверка создания уникального пользователя;
2. test_registration_existing_user() - проверка создания пользователя, который уже зарегистрирован;
3. test_registration_user_without_required_parameter() - проверка создания пользователя без заполнения одного из обязательных полей.

**Класс TestsLoginUser** - содержит тесты для проверки авторизации пользователя:
1. test_login_as_existing_user() - проверка логина под существующим пользователем;
2. test_not_login_with_invalid_email() - проверка невозможности логина с неверным логином;
3. test_not_login_with_invalid_password() - проверка невозможности логина с неверным паролем.

**Класс TestsEditUserData** - содержит тесты для проверки изменения данных пользователя:
1. test_edit_email_with_login_user() - проверка изменения email с авторизацией;
2. test_edit_name_with_login_user() - проверка изменения name с авторизацией;
3. test_edit_email_without_authorization() - проверка невозможности изменения email без авторизации;
4. test_edit_name_without_authorization() - проверка невозможности изменения name без авторизации.

**Класс TestsCreateOrder** - содержит тесты для проверки создания заказа:
1. test_create_order_with_login_and_with_ingredients() - проверка создания заказа с авторизацией и ингредиентами;
2. test_create_order_without_authorization_and_with_single_ingredients() - проверка создания заказа без авторизации и с одним ингредиентом;
3. test_not_create_order_with_login_and_without_ingredients() - проверка невозможности создания заказа без ингредиентов;
4. test_not_create_order_with_invalid_hash_ingredients() - проверка невозможности создания заказа с неверным хешем ингредиентов;
5. test_not_create_order_with_correct_and_invalid_hash_ingredients() - проверка невозможности создания заказа с наличием одновременно верных и неверных хешей ингредиентов.

**Класс TestsGetUserOrders** - содержит тесты для проверки получения списка заказов пользователя:
1. test_get_user_orders_with_login() - проверка получения заказов авторизованного пользователя;
2. test_get_user_orders_without_authorization() - проверка невозможности получения заказов неавторизованного пользователя.



### Установка зависимостей

> `$ pip install -r requirements.txt`

### Запуск отчета Allure

> `$ allure serve allure_results`
