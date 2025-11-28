
import pytest
import os
from playwright.sync_api import Page, expect
from dotenv import load_dotenv
from pages.base_page import BasePage


load_dotenv()

BASE_URL = f"{os.getenv('BASE_URL_1')}"


class MainPage(BasePage):
    url = BASE_URL

    def open(self):
        self.logger.info(f"Открываю страницу: {self.url}")
        try:
            self.page.goto(self.url)
            self.logger.info("Cтраница успешно открыта")
        except Exception as e:
            self.logger.error(f"Ошибка при открытии страницы: {e}")
            raise
