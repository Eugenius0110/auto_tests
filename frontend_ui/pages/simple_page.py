
import pytest
import os
from playwright.sync_api import Page, expect
from dotenv import load_dotenv
load_dotenv()

BASE_URL = f"{os.getenv('BASE_URL')}"

BUTTON_ENTER = '.sc-87b832e2-0.daFWkx'
BUTTON_ENTER_RESULT = 'Войти'


class SimplePage:


    def __init__(self, page: Page, headed = True):
        self.page = page

    def open(self):
        self.page.goto(BASE_URL)

    def check_button_enter_exists(self):
        button = self.page.locator(BUTTON_ENTER)
        expect(button).to_be_visible()

    def check_button_enter_result_text_is_(self, text):
        result = self.page.locator(BUTTON_ENTER)
        expect(result).to_have_text(text)


    def click_button_enter(self):
        button = self.page.locator(BUTTON_ENTER)
        button.click()
