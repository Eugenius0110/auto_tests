
import pytest
from endpoints.login_logout import LoginLogout
from payloads.login import LoginPayload
import models.login_logout as models
from http import HTTPStatus


@pytest.mark.parametrize('payload, status_code, model', [(
        LoginPayload.payload_email_not_exist,
        HTTPStatus.BAD_REQUEST,
        models.LoginEmailNotExist400)])
def test_login_email_not_exist_400(payload, status_code, model): # test_passed
    """
    Тест e-mail не найден
    :param payload:
    :param status_code:
    :param model:
    :return:
    """
    login_endpoint = LoginLogout()
    login_endpoint.login(payload)
    login_endpoint.check_response_status_code(status_code)
    login_endpoint.check_model(model)
    login_endpoint.print_response()

@pytest.mark.parametrize('payload, status_code, model', [(
        LoginPayload.payload_password_incorrect,
        HTTPStatus.BAD_REQUEST,
        models.LoginPasswordIncorrect400)])
def test_login_password_incorrect_400(payload, status_code, model): # test_passed
    login_endpoint = LoginLogout()
    login_endpoint.login(payload)
    login_endpoint.check_response_status_code(status_code)
    login_endpoint.check_model(model)
    login_endpoint.print_response()

@pytest.mark.parametrize('payload, status_code, model', [(
        LoginPayload.payload_email_empty,
        HTTPStatus.BAD_REQUEST,
        models.LoginEmailEmpty400)])
def test_login_email_empty_400(payload, status_code, model): # test_passed
    login_endpoint = LoginLogout()
    login_endpoint.login(payload)
    login_endpoint.check_response_status_code(status_code)
    login_endpoint.check_model(model)
    login_endpoint.print_response()

@pytest.mark.parametrize('payload, status_code, model', [(
        LoginPayload.payload_login_success,
        HTTPStatus.OK,
        models.LoginSuccess200)])
@pytest.mark.smoke
def test_login_200(payload, status_code, model): # test_passed
    login_endpoint = LoginLogout()
    login_endpoint.login(payload)
    login_endpoint.check_response_status_code(status_code)
    login_endpoint.check_model(model)
    login_endpoint.print_response()

@pytest.mark.parametrize('payload, status_code, model', [(
        LoginPayload.payload_login_success,
        HTTPStatus.OK,
        models.LogoutSuccess200)])
@pytest.mark.smoke
def test_logout_200(payload, status_code, model): # test_passed
    logout_endpoint = LoginLogout()
    logout_endpoint.login(payload)
    logout_endpoint.check_response_status_code(status_code)
    logout_endpoint.logout()
    logout_endpoint.check_response_status_code(status_code)
    logout_endpoint.check_model(model)
    logout_endpoint.print_response()

@pytest.mark.parametrize('payload, status_code, model', [(
        LoginPayload.payload_login_success,
        HTTPStatus.OK,
        models.RefreshTokenSuccess200)])
@pytest.mark.smoke
def test_refresh_token_200(payload, status_code, model): # test_passed
    refresh_endpoint = LoginLogout()
    refresh_endpoint.login(payload)
    refresh_endpoint.check_response_status_code(status_code)
    refresh_endpoint.refresh()
    refresh_endpoint.check_response_status_code(status_code)
    refresh_endpoint.check_model(model)
    refresh_endpoint.print_response()






