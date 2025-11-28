

import logging
from playwright.sync_api import Page, expect, Locator
#from playwright.async_api import Page, expect, Locator
from utils.logger import logger


class BasePage:

    url = None
    def __init__(self, page: Page):
        self.page = page
        self.logger = logger.getChild(self.__class__.__name__)
        self.logger.info(f"Инициализована страница")


    def get_locator(self, element_dict: dict) -> Locator:
        element = self.page.get_by_role("button", name="Войти")
        # if element_dict.get('data-testid'):
        #     element = self.page.get_by_test_id(element_dict.get('data-testid'))
        # else:
        #     element = self.page.locator(element_dict.get('selector'))
        return element

    def element_click(self, element_dict: dict):
        element = self.get_locator(element_dict)
        element.click()
        print(f"{element_dict.get('description')} clickable")

    def check_element_attached(self, element_dict: dict): # проверяем, что элемент прикреплен к DOM
        self.logger.info(f"Проверка attached")
        element = self.get_locator(element_dict)
        expect(element).to_be_attached()
        self.logger.info(f"Элемент attached DOM: {element_dict.get('description')}")

    def check_element_visible(self, element_dict: dict): # проверяем, что элемент видим
        self.logger.info(f"Проверка visible")
        element = self.get_locator(element_dict)
        expect(element).to_be_visible()
        self.logger.info(f"Элемент visible: {element_dict.get('description')}")

    def check_element_enabled(self, element_dict: dict): # проверяем, что элемент доступен
        self.logger.info(f"Проверка enable")
        element = self.get_locator(element_dict)
        expect(element).to_be_enabled()
        self.logger.info(f"Элемент enabled: {element_dict.get('description')}")


    def check_element_has_text(self, element_dict: dict): # проверяем, что элемент содержит текст
        element = self.get_locator(element_dict)
        expect(element).to_have_text(element_dict.get('text'))
        print(f"{element_dict.get('description')} has text: {element_dict.get('text')}")

    async def check_element_editable(self, element_dict: dict): # проверяем, что элемент редактируемый
        element = self.get_locator(element_dict)
        expect(element).to_be_editable()
        print(f"{element_dict.get('description')} editable")

    def check_element_focus(self, element_dict: dict):  # проверяем, что элемент в фокусе
        element = self.get_locator(element_dict)
        element.focus()
        expect(element).to_be_focused()
        print(f"{element_dict.get('description')} focus")

    def check_element_click(self, element_dict: dict): # проверяем, что на элемент можно кликнуть
        element = self.get_locator(element_dict)
        element.click()
        print(f"{element_dict.get('description')} clickable")

    def check_test(self):
        pass