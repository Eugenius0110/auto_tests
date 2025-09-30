
import requests
from endpoints.check_status_code_and_model import BaseApi


class SetPassword(BaseApi):

    def set_password(self, payload):
        self.response = requests.post(f"{self.BASE_URL}/api/auth/set-password/", payload)


