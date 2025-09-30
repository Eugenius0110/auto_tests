import os
from faker import Faker
from dotenv import load_dotenv
from yandex_mail_api.get_code_from_email import GetConfirmCode

load_dotenv()
fake = Faker()


class ResetAndSetPasswordPayload:


    payload_reset_password = {
        "email": f"{os.getenv('TEST_EMAIL_USER')}",
    }

    payload_reset_password_email_not_exist = {
        "email": f"{os.getenv('TEST_EMAIL_USER_2')}",
    }

    email_incorrect = "usermail.com"
    payload_reset_password_email_incorrect = {
        "email": email_incorrect,
    }

    # @staticmethod
    # def get_confirm_code():
    #     get_confirm_code = GetConfirmCode.get_confirm_code_from_latest_email()
    #     payload_confirm_code = {
    #         "email": f"{os.getenv('TEST_EMAIL_USER')}",
    #         "confirmation_code": f"{get_confirm_code}"
    #     }
    #     return payload_confirm_code


    payload_set_password = {
        "new_password": f"{os.getenv('TEST_PASSWORD')}",
        "new_password_confirm": f"{os.getenv('TEST_PASSWORD')}"
    }

