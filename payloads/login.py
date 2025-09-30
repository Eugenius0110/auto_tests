import os
from faker import Faker
from dotenv import load_dotenv

load_dotenv()
fake = Faker()


class LoginPayload:


    payload_login_success = {
        "email": f"{os.getenv('TEST_EMAIL_USER')}",
        "password": f"{os.getenv('TEST_PASSWORD')}"
    }

    payload_email_not_exist = {
        "email": f"{os.getenv('TEST_EMAIL_USER_2')}",
        "password": f"{os.getenv('TEST_PASSWORD')}"
    }

    payload_password_incorrect = {
        "email": f"{os.getenv('TEST_EMAIL_USER_2')}",
        "password": f"{os.getenv('TEST_PASSWORD')}incorrect"
    }

    payload_email_empty = {
        "email": f"",
        "password": f"{os.getenv('TEST_PASSWORD')}"
    }



