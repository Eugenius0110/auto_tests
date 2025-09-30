
import requests
from endpoints.check_status_code_and_model import BaseApi


class SignupUser(BaseApi):
    def __init__(self):
        self.response = None

    def new_signup_user(self, payload): #, payload
        self.response = requests.post(f"{self.BASE_URL}/api/auth/signup/", payload)
