
import pytest
import os
from playwright.sync_api import Page, expect
from dotenv import load_dotenv
from pages.base_page import BasePage


load_dotenv()

BASE_URL = f"{os.getenv('BASE_URL')}"


class MainPage(BasePage):
    url = BASE_URL

