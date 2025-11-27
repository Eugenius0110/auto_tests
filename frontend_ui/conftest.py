
import pytest
from playwright.sync_api import Page, expect

from pages.main_page import MainPage


@pytest.fixture()
def main_page(page: Page) -> MainPage:
    main_page = MainPage(page)
    main_page.open()
    return main_page

    #page.set_viewport_size({'height': 800, 'width': 1000})
