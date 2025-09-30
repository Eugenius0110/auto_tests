
import requests
import pytest
from endpoints.check_status_code_and_model import BaseApi


class LoginLogout(BaseApi):
    def __init__(self):
        self.response = None
        self.access_token = None
        self.refresh_token = None


    def login(self, payload):
        self.response = requests.post(
            url=f"{self.BASE_URL}/api/auth/login/",
            json=payload
        )
        if 'access_token' in self.response.json():
            self.access_token = self.response.json()['access_token']
            self.refresh_token = self.response.json()['refresh_token']

    def logout(self):
        payload_refresh_token = {
            "refresh_token": f"{self.refresh_token}"
        }
        self.response = requests.post(
            url=f"{self.BASE_URL}/api/auth/logout/",
            json=payload_refresh_token,
            headers= {
                "Authorization": f"Bearer {self.access_token}"

            }
        )

    def refresh(self):
        payload_refresh_token = {
            "refresh_token": f"{self.refresh_token}"
        }
        self.response = requests.post(
            url=f"{self.BASE_URL}/api/token/refresh/",
            json=payload_refresh_token,
            headers= {
                "Authorization": f"Bearer {self.access_token}"
            }
        )
