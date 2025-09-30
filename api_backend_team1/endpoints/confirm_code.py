
import requests
from endpoints.check_status_code_and_model import BaseApi


class ConfirmCode(BaseApi):

    def confirm_code(self, payload):
        self.response = requests.post(f"{self.BASE_URL}/api/auth/confirm-code/", payload)

