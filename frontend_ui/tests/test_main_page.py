
import sys
import os
from playwright.sync_api import Page, expect
from pathlib import Path
from playwright.sync_api import sync_playwright

# current_dir = Path(__file__).parent
# frontend_root = current_dir.parent
# sys.path.insert(0, str(frontend_root))
# from pages.simple_page import SimplePage

from pages.main_page import MainPage
from elements.locators import MainPageLocators


def test_button_enter_exists(page: Page):
    main_page = MainPage(page)
    main_page.open()
    main_page.check_element_visible(MainPageLocators.button_enter['selector'], MainPageLocators.button_enter['description'] )
    #main_page.check_element_attached()

# def test_simple_click(page: Page):
#     simple_page = SimplePage(page)
#     simple_page.open()
#     simple_page.click_button()
#     simple_page.check_result_text_is_('Submitted')

