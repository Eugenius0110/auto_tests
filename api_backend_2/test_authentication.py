import time

import pytest
import requests
import allure
#from requests.auth import HTTPBasicAuth

BASE_URL = "http://server-name:8080"
phoneNumberOrEmail = "eug0110@mail.ru"
password = "vWjk1^S!J6"

# pytest -s -v :)

# регистрация нового пользователя
class TestRegistrationNewUser:

    @pytest.fixture()
    def fixt_registration_response(self, firstname, lastname, phonenumber, email):
        response = requests.post(
        url=f"{BASE_URL}/api/auth/registration",
        json={
            "firstName": firstname,
            "lastName": lastname,
            "phoneNumber": phonenumber,
            "email": email
        }
        )
        print(f"\n>> {"-" * 60} \n{response.status_code} {response.json()} \n>> {"-" * 60}")
        return response


    # код 200, на почту выслан код верификации
    #@allure.title("Регистрация нового пользователя title")
    #@allure.feature("Регистрация нового пользователя")
    @pytest.mark.parametrize('firstname, lastname, phonenumber, email',
        [("Eugene_autotest", "Kotov_autotest", "+79781234561", "eug01001@gmail.com")])
    def test_code_send_status_code_200(self, fixt_registration_response):
        response = fixt_registration_response
        assert response.status_code == 200, f"Ожидался 200, а пришел {response.status_code}"
        assert "Content-Type" in response.headers
        assert response.headers['Content-Type'] == "application/json", f"Header {response.headers['Content-Type']}"
        assert response.json()
        assert set(response.json()) == {'message'}, f"Содержится {set(response.json())}"
        assert isinstance(response.json()['message'], str)
        assert "код верификации" in response.json()['message']

        #assert response.elapsed.total_seconds() < 1.0 # время ответа api

    # код 429, код уже выслан на почту
    @pytest.mark.parametrize('firstname, lastname, phonenumber, email',
        [("Eugene_autotest", "Kotov_autotest", "+79781234561", "eug01001@gmail.com")])
    def test_code_already_send_status_code_429(self, fixt_registration_response):
        response = fixt_registration_response
        assert response.status_code == 429, f"Ожидался 429, а пришел {response.status_code}"
        assert "Content-Type" in response.headers
        assert response.headers['Content-Type'] == "application/json", f"Header {response.headers['Content-Type']}"
        assert response.json()
        assert set(response.json()) == {'message'}, f"Содержится {set(response.json())}"
        assert isinstance(response.json()['message'], str)
        assert "Код уже был отправлен. Повторная отправка доступна через" in response.json()['message']


    # код 400, пользователь с таким номером уже существует
    @pytest.mark.parametrize('firstname, lastname, phonenumber, email',
        [("Eugene_autotest", "Kotov_autotest", "+79781234561", "eug01002@gmail.com")])
    def test_user_already_exists_status_code_400(self, fixt_registration_response):
        response = fixt_registration_response
        assert response.status_code == 400, f"Ожидался 400, а пришел {response.status_code}"
        assert "Content-Type" in response.headers
        assert response.headers['Content-Type'] == "application/json", f"Header {response.headers['Content-Type']}"
        assert response.json()
        assert set(response.json()) == {'message'}, f"Содержится {set(response.json())}"
        assert isinstance(response.json()['message'], str)
        assert "Пользователь с таким номером телефона уже существует." in response.json()['message']

    # код 400, поле firstname пустое
    @pytest.mark.parametrize('firstname, lastname, phonenumber, email',
        [("", "Kotov_autotest", "+79781234561", "eug01001@gmail.com")])
    def test_firstname_is_empty_status_code_400(self, fixt_registration_response):
        response = fixt_registration_response
        assert response.status_code == 400, f"Ожидался 400, а пришел {response.status_code}"
        assert "Content-Type" in response.headers
        assert response.headers['Content-Type'] == "application/json", f"Header {response.headers['Content-Type']}"
        assert response.json()
        assert set(response.json()) == {'message'}, f"Содержится {set(response.json())}"
        assert isinstance(response.json()['message'], str)
        assert "Ошибка валидации: firstName - Обязательное поле;" in response.json()['message']

    # код 400, поле lastname пустое
    @pytest.mark.parametrize('firstname, lastname, phonenumber, email',
        [("Eugene_autotest", "", "+79781234561", "eug01001@gmail.com")])
    def test_lastname_is_empty_status_code_400(self, fixt_registration_response):
        response = fixt_registration_response
        assert response.status_code == 400, f"Ожидался 400, а пришел {response.status_code}"
        assert "Content-Type" in response.headers
        assert response.headers['Content-Type'] == "application/json", f"Header {response.headers['Content-Type']}"
        assert response.json()
        assert set(response.json()) == {'message'}, f"Содержится {set(response.json())}"
        assert isinstance(response.json()['message'], str)
        assert "Ошибка валидации: lastName - Обязательное поле;" in response.json()['message']

    # код 400, поле phoneNumber пустое
    @pytest.mark.parametrize('firstname, lastname, phonenumber, email',
        [("Eugene_autotest", "Kotov_autotest", "", "eug01001@gmail.com")])
    def test_phone_number_is_empty_status_code_400(self, fixt_registration_response):
        response = fixt_registration_response
        assert response.status_code == 400, f"Ожидался 400, а пришел {response.status_code}"
        assert "Content-Type" in response.headers
        assert response.headers['Content-Type'] == "application/json", f"Header {response.headers['Content-Type']}"
        assert response.json()
        assert set(response.json()) == {'message'}, f"Содержится {set(response.json())}"
        assert isinstance(response.json()['message'], str)
        assert "phoneNumber - Номер должен быть в формате +7... и содержать 11 цифр;" in response.json()['message']


    # код 400, поле email пустое
    @pytest.mark.parametrize('firstname, lastname, phonenumber, email',
        [("Eugene_autotest", "Kotov_autotest", "+79781234561", "")])
    def test_email_is_empty_status_code_400(self, fixt_registration_response):
        response = fixt_registration_response
        assert response.status_code == 400, f"Ожидался 400, а пришел {response.status_code}"
        assert "Content-Type" in response.headers
        assert response.headers['Content-Type'] == "application/json", f"Header {response.headers['Content-Type']}"
        assert response.json()
        assert set(response.json()) == {'message'}, f"Содержится {set(response.json())}"
        assert isinstance(response.json()['message'], str)
        assert "email - Неверный формат email" in response.json()['message']
        assert "email - Обязательное поле" in response.json()['message']

class TestConfirmMailandPassword:

    CODE = "778029"

    @pytest.fixture()
    def fixt_confirm_mail_response(self, verifycode):
        response = requests.post(
            url=f"{BASE_URL}/api/auth/registration/confirm-mail",
            json={
                "verifyCode": verifycode
            }
        )
        print(f"\n>> {"-" * 60} \n{response.status_code} {response.json()} \n>> {"-" * 60}")
        #self.access_token =
        return response


    @pytest.fixture()
    def fixt_confirm_password_response(self, access_token, email, password, confirm_password):
        response = requests.post(
            url=f"{BASE_URL}/api/auth/registration/confirm-password",
            headers={
                "Authorization": f"Bearer {access_token}"
            },
            json={
                "email": email,
                "password": password,
                "confirmPassword": confirm_password
            }
        )
        print(f"\n>> {"-" * 60} \n{response.status_code} {response.json()} \n>> {"-" * 60}")
        return response

    # код 200, подтверждение email и установка пароля, пароли не совпадают
    @pytest.mark.parametrize('verifycode', [CODE])
    def test_verify_mail_and_set_password_status_code_200_and_password_not_match_status_code_400(self, fixt_confirm_mail_response):
        response = fixt_confirm_mail_response
        assert response.status_code == 200, f"Ожидался 200, а пришел {response.status_code}"
        assert "Content-Type" in response.headers
        assert response.headers['Content-Type'] == "application/json", f"Header {response.headers['Content-Type']}"
        assert response.json(), "Ответ не json"
        assert set(response.json()) == {'message', 'accessToken'}, f"Содержится {set(response.json())}"
        assert isinstance(response.json()['message'], str)
        assert isinstance(response.json()['accessToken'], str)
        assert ("Email успешно подтвержден. Пароль будет отправлен на вашу электронную почту в течение 10 минут, "
                "если вы не завершите регистрацию (ввод пароля)") in response.json()['message']
        access_token = response.json()['accessToken']

        # код 400, пароли не совпадают
        response = requests.post(
            url=f"{BASE_URL}/api/auth/registration/confirm-password",
            headers={
                "Authorization": f"Bearer {access_token}"
                    },
            json={
               "email": "eug01001@gmail.com",
               "password": "Ab12345678#",
               "confirmPassword": "Ab12345678#1"
               }
            )
        assert response.status_code == 400, f"Ожидался 400, а пришел {response.status_code}"
        assert "Content-Type" in response.headers
        assert response.headers['Content-Type'] == "application/json", f"Header {response.headers['Content-Type']}"
        assert response.json(), "Ответ не json"
        assert set(response.json()) == {'message'}, f"Содержится {set(response.json())}"
        assert isinstance(response.json()['message'], str)
        assert "Пароли не совпадают" in response.json()['message']

        # если 200, устанавливаем пароль
        response = requests.post(
            url=f"{BASE_URL}/api/auth/registration/confirm-password",
            headers={
                "Authorization": f"Bearer {access_token}"
            },
            json={
                "email": "eug01001@gmail.com",
                "password": "Ab12345678#",
                "confirmPassword": "Ab12345678#"
            }
        )
        #
        assert response.status_code == 200, f"Ожидался 200, а пришел {response.status_code}"
        assert "Content-Type" in response.headers
        assert response.headers['Content-Type'] == "application/json", f"Header {response.headers['Content-Type']}"
        assert response.json(), "Ответ не json"
        assert set(response.json()) == {'message'}, f"Содержится {set(response.json())}"
        assert isinstance(response.json()['message'], str)
        assert "Пароль установлен" in response.json()['message']

    # код 400, неверный код
    #@pytest.mark.skip(reason="Пропуск тест")
    @pytest.mark.parametrize('verifycode', ["123456"])
    def test_verify_mail_invalid_code_status_code_400(self, fixt_confirm_mail_response):
        response = fixt_confirm_mail_response
        assert response.status_code == 400, f"Ожидался 400, а пришел {response.status_code}"
        assert "Content-Type" in response.headers
        assert response.headers['Content-Type'] == "application/json", f"Header {response.headers["Content-Type"]}"
        assert response.json(), "Ответ не json"
        assert set(response.json()) == {'message'}, f"Содержится {set(response.json())}"
        assert isinstance(response.json()['message'], str)
        assert "Неверный код подтверждения" in response.json()["message"]

    # код 400, передан пустой код
    #@pytest.mark.skip
    @pytest.mark.parametrize('verifycode', [""])
    def test_verify_mail_code_is_empty_status_code_400(self, fixt_confirm_mail_response):
        response = fixt_confirm_mail_response
        assert response.status_code == 400, f"Ожидался 400, а пришел {response.status_code}"
        assert "Content-Type" in response.headers
        assert response.headers['Content-Type'] == "application/json", f"Header {response.headers["Content-Type"]}"
        assert response.json(), "Ответ не json"
        assert set(response.json()) == {'message'}, f"Содержится {set(response.json())}"
        assert isinstance(response.json()['message'], str)
        assert "Код подтверждения не может быть пустым" in response.json()["message"]

    # код 400, недействительный токен
    #@pytest.mark.skip
    @pytest.mark.parametrize('access_token, email, password, confirm_password',
        [("invalid_token", "eug01001@gmail.com", "Ab12345678#", "Ab12345678#")])
    def test_set_password_invalid_token_status_code_400(self, fixt_confirm_password_response):
        response = fixt_confirm_password_response
        assert response.status_code == 401, f"Ожидался 401, а пришел {response.status_code}"
        assert "Content-Type" in response.headers
        assert response.headers['Content-Type'] == "application/json", f"Header {response.headers['Content-Type']}"
        assert response.json(), "Ответ не json"
        assert set(response.json()) == {'message'}, f"Содержится {set(response.json())}"
        assert isinstance(response.json()['message'], str)
        assert "Недействительный токен" in response.json()['message']

    # код 401, пустой токен
    #@pytest.mark.skip
    @pytest.mark.parametrize('access_token, email, password, confirm_password',
        [("", "eug01001@gmail.com", "Ab12345678#", "Ab12345678#")])
    def test_set_password_token_is_empty_status_code_400(self, fixt_confirm_password_response):
        response = fixt_confirm_password_response
        assert response.status_code == 401, f"Ожидался 401, а пришел {response.status_code}"
        assert "Content-Type" in response.headers
        assert response.headers['Content-Type'] == "application/json", f"Header {response.headers['Content-Type']}"
        assert response.json(), "Ответ не json"
        assert set(response.json()) == {'message'}, f"Содержится {set(response.json())}"
        assert isinstance(response.json()['message'], str)
        assert "Токен отсутствует" in response.json()['message']

    # код 400, ошибка валидации
    #@pytest.mark.skip
    @pytest.mark.parametrize('access_token, email, password, confirm_password',
        [("accessToken", "eug01001@gmail.com", "123456", "123456")])
    def test_set_password_validation_error_status_code_400(self, fixt_confirm_password_response):
        response = fixt_confirm_password_response
        assert response.status_code == 400, f"Ожидался 400, а пришел {response.status_code}"
        assert "Content-Type" in response.headers
        assert response.headers['Content-Type'] == "application/json", f"Header {response.headers['Content-Type']}"
        assert response.json(), "Ответ не json"
        assert set(response.json()) == {'message'}, f"Содержится {set(response.json())}"
        assert isinstance(response.json()['message'], str)
        assert "Ошибка валидации:" in response.json()['message']
        assert ("password - Пароль должен содержать 10 символов, хотя бы одну заглавную букву, "
                "одну цифру и один специальный символ") in response.json()['message']
        assert ("password - Пароль должен содержать минимум 10 символов") in response.json()['message']

class TestLoginLogout:

    @pytest.fixture()
    def fixt_login_get_access_token(self, phone_email, password):
        response = requests.post(
            url=f"{BASE_URL}/api/auth/login",
            json={
                "phoneNumberOrEmail": phone_email,
                "password": password
            }
        )
        print(f"\n>> {"-" * 60} \n{response.status_code} {response.json()} \n>> {"-" * 60}")
        return response

    @pytest.fixture()
    def fixt_logout(self, fixt_login_get_access_token):
        response = requests.post(
            url=f"{BASE_URL}/api/auth/logout",
            headers={
                "Authorization": f"Bearer {fixt_login_get_access_token.json()['accessToken']}"
            }
        )
        print(f"\n>> {"-" * 60} \n{response.status_code} {response.json()} \n>> {"-" * 60}")
        return response


    @pytest.mark.parametrize('phone_email, password',
                            [("eug0110@mail.ru", "vWjk1^S!J6")])
    def test_login_status_code_200(self, fixt_login_get_access_token):
        response = fixt_login_get_access_token
        assert response.status_code == 200, f"Ожидался 200, а пришел {response.status_code}"
        assert "Content-Type" in response.headers
        assert response.headers['Content-Type'] == "application/json", f"Header {response.headers['Content-Type']}"
        assert response.json(), "Ответ не json"
        assert set(response.json()) == {'accessToken', 'refreshToken'}, f"Содержится {set(response.json())}"
        assert isinstance(response.json()['accessToken'], str)
        assert isinstance(response.json()['refreshToken'], str)
        assert response.json()['accessToken'] # не пустой
        assert response.json()['refreshToken'] # не пустой

    @pytest.mark.parametrize('phone_email, password',
                             [("", "vWjk1^S!J6")])
    def test_login_phoneNumberOrEmail_is_empty_status_code_400(self, fixt_login_get_access_token):
        response = fixt_login_get_access_token
        assert response.status_code == 400, f"Ожидался 400, а пришел {response.status_code}"
        assert "Content-Type" in response.headers
        assert response.headers['Content-Type'] == "application/json", f"Header {response.headers['Content-Type']}"
        assert response.json(), "Ответ не json"
        assert set(response.json()) == {'message'}, f"Содержится {set(response.json())}"
        assert isinstance(response.json()['message'], str)
        assert "Ошибка валидации: phoneNumberOrEmail - Обязательное поле" in response.json()['message']

    @pytest.mark.parametrize('phone_email, password',
                             [("eug0110@mail.ru", "")])
    def test_login_password_is_empty_status_code_400(self, fixt_login_get_access_token):
        response = fixt_login_get_access_token
        assert response.status_code == 400, f"Ожидался 400, а пришел {response.status_code}"
        assert "Content-Type" in response.headers
        assert response.headers['Content-Type'] == "application/json", f"Header {response.headers['Content-Type']}"
        assert response.json(), "Ответ не json"
        assert set(response.json()) == {'message'}, f"Содержится {set(response.json())}"
        assert isinstance(response.json()['message'], str)
        assert "Ошибка валидации: password - Обязательное поле" in response.json()['message']

    @pytest.mark.parametrize('phone_email, password',
                             [("eug0110@mail.ru", "vWjk1^S!J6")])
    def test_logout_status_code_200(self, fixt_logout):
        response = fixt_logout
        assert response.status_code == 200, f"Ожидался 200, а пришел {response.status_code}"
        assert "Content-Type" in response.headers
        assert response.headers['Content-Type'] == "application/json", f"Header {response.headers['Content-Type']}"
        assert response.json(), "Ответ не json"
        assert set(response.json()) == {'message'}, f"Содержится {set(response.json())}"
        assert isinstance(response.json()['message'], str)
        assert "Выход выполнен успешно" in response.json()['message']

class TestForgotPassword:

    @pytest.fixture()
    def fixt_forgot_password(self, emailOrPhoneNumber):
        response = requests.post(
            url=f"{BASE_URL}/api/auth/forgot-password",
            json={
                "emailOrPhoneNumber": emailOrPhoneNumber
            }
        )
        print(f"\n>> {"-" * 60} \n{response.status_code} {response.json()} \n>> {"-" * 60}")
        return response

    @pytest.fixture()
    def fixt_login_get_access_token(self, phone_email, password):
        response = requests.post(
            url=f"{BASE_URL}/api/auth/login",
            json={
                "phoneNumberOrEmail": phone_email,
                "password": password
            }
        )
        print(f"\n>> {"-" * 60} \n{response.status_code} {response.json()} \n>> {"-" * 60}")
        return response

    @allure.title("200, запрос на сброс пароля отправлен на ваш email")
    @pytest.mark.parametrize('emailOrPhoneNumber', ["eug0110@mail.ru"])
    def test_forgot_password_status_code_200(self, fixt_forgot_password):
        response = fixt_forgot_password
        assert response.status_code == 200, f"Ожидался 200, а пришел {response.status_code}"
        assert "Content-Type" in response.headers
        assert response.headers['Content-Type'] == "application/json", f"Header {response.headers['Content-Type']}"
        assert response.json(), "Ответ не json"
        assert set(response.json()) == {'message'}, f"Содержится {set(response.json())}"
        assert isinstance(response.json()['message'], str)
        assert "Запрос на сброс пароля отправлен на ваш email" in response.json()['message']

    @allure.title("Запрос уже отправлен")
    @pytest.mark.parametrize('emailOrPhoneNumber', ["eug0110@mail.ru"])
    def test_forgot_password_status_code_429(self, fixt_forgot_password):
        response = fixt_forgot_password
        assert response.status_code == 429, f"Ожидался 429, а пришел {response.status_code}"
        assert "Content-Type" in response.headers
        assert response.headers['Content-Type'] == "application/json", f"Header {response.headers['Content-Type']}"
        assert response.json(), "Ответ не json"
        assert set(response.json()) == {'message'}, f"Содержится {set(response.json())}"
        assert isinstance(response.json()['message'], str)
        assert "Запрос на сброс пароля уже отправлен. Повторная отправка доступна через" in response.json()['message']

    @allure.title("400, поле emailOrPhoneNumber пустое")
    @pytest.mark.parametrize('emailOrPhoneNumber', [""])
    def test_forgot_password_emailOrPhoneNumber_is_empty_status_code_400(self, fixt_forgot_password):
        response = fixt_forgot_password
        assert response.status_code == 400, f"Ожидался 400, а пришел {response.status_code}"
        assert "Content-Type" in response.headers
        assert response.headers['Content-Type'] == "application/json", f"Header {response.headers['Content-Type']}"
        assert response.json(), "Ответ не json"
        assert set(response.json()) == {'message'}, f"Содержится {set(response.json())}"
        assert isinstance(response.json()['message'], str)
        assert "Ошибка валидации: emailOrPhoneNumber - Нужно указать email или номер телефона" in response.json()['message']

    @allure.title("404, пользователь не найден")
    @pytest.mark.parametrize('emailOrPhoneNumber', ["eug01101@mail.ru"])
    def test_forgot_password_user_not_found_is_empty_status_code_400(self, fixt_forgot_password):
        response = fixt_forgot_password
        assert response.status_code == 404, f"Ожидался 404, а пришел {response.status_code}"
        assert "Content-Type" in response.headers
        assert response.headers['Content-Type'] == "application/json", f"Header {response.headers['Content-Type']}"
        assert response.json(), "Ответ не json"
        assert set(response.json()) == {'message'}, f"Содержится {set(response.json())}"
        assert isinstance(response.json()['message'], str)
        assert "Пользователь не найден" in response.json()['message']

    @allure.title("401, недействительный токен")
    @pytest.mark.parametrize('access_token', ["access_token"])
    def test_reset_password_status_code_401(self, access_token):
        response = requests.get(
            url=f"{BASE_URL}/api/auth/reset-password",
            params={"token": f"{access_token}"
                    }
        )
        assert response.status_code == 401, f"Ожидался 401, а пришел {response.status_code}"
        assert "Content-Type" in response.headers
        assert response.headers['Content-Type'] == "application/json", f"Header {response.headers['Content-Type']}"
        assert response.json(), "Ответ не json"
        assert set(response.json()) == {'message'}, f"Содержится {set(response.json())}"
        assert isinstance(response.json()['message'], str)
        assert "Недействительный токен" in response.json()['message']

    # запуск с -s: pytest -s .\test_authentication.py::TestForgotPassword (-s чтобы pytest не перехватывал ввод:)
    @pytest.mark.parametrize('access_token', ["access_token"])
    def test_reset_password_status_code_200(self, access_token):
        access_token = input("Enter access_token: ")
        response = requests.get(
            url=f"{BASE_URL}/api/auth/reset-password",
            params={"token": f"{access_token}"
            }
        )
        print(f"\n>> {"-" * 60} \n{response.status_code} {response.json()} \n>> {"-" * 60}")
        assert response.status_code == 200, f"Ожидался 200, а пришел {response.status_code}"
        assert "Content-Type" in response.headers
        assert response.headers['Content-Type'] == "application/json", f"Header {response.headers['Content-Type']}"
        assert response.json(), "Ответ не json"
        assert set(response.json()) == {'message'}, f"Содержится {set(response.json())}"
        assert isinstance(response.json()['message'], str)
        assert "Новый пароль отправлен на email" in response.json()['message']

