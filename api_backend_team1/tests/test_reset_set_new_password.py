import pytest
from faker import Faker
from dotenv import load_dotenv
from endpoints.reset_set_new_password import ResetAndSetNewPassword
from payloads.reset_and_set_new_password import ResetAndSetPasswordPayload
from payloads.create_user import ConfirmCodePayload

load_dotenv()
fake = Faker()

import pytest
from faker import Faker
from dotenv import load_dotenv
from endpoints.login_logout import LoginLogout
from payloads.login import LoginPayload

load_dotenv()
fake = Faker()


def test_reset_password_email_not_exist_400(): #pass
    resetpassword_endpoint = ResetAndSetNewPassword()
    resetpassword_endpoint.reset_password(ResetAndSetPasswordPayload.payload_reset_password_email_not_exist)
    resetpassword_endpoint.check_response_status_code(400)
    resetpassword_endpoint.check_reset_password_email_not_exist_model_400()

def test_reset_password_email_incorrect_400(): #pass
    resetpassword_endpoint = ResetAndSetNewPassword()
    resetpassword_endpoint.reset_password(ResetAndSetPasswordPayload.payload_reset_password_email_incorrect)
    resetpassword_endpoint.check_response_status_code(400)
    resetpassword_endpoint.check_reset_password_email_incorrect_400()

def test_reset_password_success_200(): #pass
    resetpassword_endpoint = ResetAndSetNewPassword()
    resetpassword_endpoint.reset_password(ResetAndSetPasswordPayload.payload_reset_password)
    resetpassword_endpoint.print_response()
    resetpassword_endpoint.check_response_status_code(200)
    resetpassword_endpoint.check_reset_password_model_success_200()

def test_reset_password_limit_attempt_429():
    pass

def test_verify_code_wrong_400(): #pass
    verifycode_endpoint = ResetAndSetNewPassword()
    verifycode_endpoint.verify_reset_code(ConfirmCodePayload.payload_confirm_code_invalid)
    verifycode_endpoint.print_response()
    verifycode_endpoint.check_response_status_code(400)
    verifycode_endpoint.check_verify_code_success_wrong_400()

def test_verify_code_success_200():
    verifycode_endpoint = ResetAndSetNewPassword()
    verifycode_endpoint.verify_reset_code(ConfirmCodePayload.get_confirm_code())
    verifycode_endpoint.print_response()
    verifycode_endpoint.check_response_status_code(200)
    verifycode_endpoint.check_verify_code_success_200()

def test_set_new_password_success_200():
    setnewpassword_endpoint = ResetAndSetNewPassword()
    setnewpassword_endpoint.set_new_password(ResetAndSetPasswordPayload.payload_set_password)
    setnewpassword_endpoint.print_response()
    setnewpassword_endpoint.check_response_status_code(200)
    #setnewpassword_endpoint.set

