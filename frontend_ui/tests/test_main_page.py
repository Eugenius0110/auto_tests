
import sys
import os
import pytest
from playwright.sync_api import Page
from pathlib import Path
from playwright.sync_api import sync_playwright

# current_dir = Path(__file__).parent
# frontend_root = current_dir.parent
# sys.path.insert(0, str(frontend_root))
# from pages.simple_page import SimplePage

from pages.main_page import MainPage
from elements.selectors import MainPageSelectors


@pytest.mark.ui
@pytest.mark.smoke
@pytest.mark.parametrize('element_dict',
                         [MainPageSelectors.button_enter]
                         )
def test_button_enter_exists(page: Page, element_dict):
    main_page = MainPage(page)
    main_page.open()
    main_page.check_element_attached(element_dict)
    main_page.check_element_visible(element_dict)
    main_page.check_element_enabled(element_dict)
    main_page.check_element_has_text(element_dict)
    main_page.check_element_focus(element_dict)







# def test_simple_click(page: Page):
#     simple_page = SimplePage(page)
#     simple_page.open()
#     simple_page.click_button()
#     simple_page.check_result_text_is_('Submitted')

