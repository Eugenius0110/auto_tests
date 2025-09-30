
import requests
from endpoints.check_status_code_and_model import BaseApi


class ResetAndSetNewPassword(BaseApi):


    def reset_password(self, payload):
        self.response = requests.post(f"{self.BASE_URL}/api/auth/reset-password/", payload)

    def verify_reset_code(self, payload):
        self.response = requests.post(f"{self.BASE_URL}/api/auth/verify-reset-code/", payload)

    def set_new_password(self, payload):
        self.response = requests.post(f"{self.BASE_URL}/api/auth/set-new-password/", payload)
