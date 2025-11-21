
from playwright.sync_api import Page, expect




import sys
import os
from pathlib import Path
from playwright.sync_api import sync_playwright

# current_dir = Path(__file__).parent
# frontend_root = current_dir.parent
# sys.path.insert(0, str(frontend_root))
# from pages.simple_page import SimplePage

from pages.simple_page import SimplePage


def test_button_enter_exists(page: Page):
    simple_page = SimplePage(page)
    simple_page.open()
    simple_page.check_button_enter_exists()
    simple_page.check_button_enter_result_text_is_('Войти')

# def test_simple_click(page: Page):
#     simple_page = SimplePage(page)
#     simple_page.open()
#     simple_page.click_button()
#     simple_page.check_result_text_is_('Submitted')

