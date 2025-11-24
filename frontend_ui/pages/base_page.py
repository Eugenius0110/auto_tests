from tkinter.font import names

from playwright.sync_api import Page, expect


class BasePage:

    url = None
    def __init__(self, page: Page):
        self.page = page

    def open(self):
        if self.url:
            self.page.goto(self.url)

    def get_locator(self, element_dict: dict):
        if element_dict.get('role') and element_dict.get('text'):
            element = self.page.get_by_role(element_dict.get('role'), name=element_dict.get('text'))
        else:
            element = self.page.locator(element_dict.get('selector'))
        return element

    def check_element_attached(self, element_dict: dict): # проверяем, что элемент прикреплен к DOM
        element = self.get_locator(element_dict)
        expect(element).to_be_attached()
        print(f"{element_dict.get('description')} attached DOM")

    def check_element_visible(self, element_dict: dict): # проверяем, что элемент видим
        element = self.get_locator(element_dict)
        expect(element).to_be_visible()
        print(f"{element_dict.get('description')} visible")

    def check_element_enabled(self, element_dict: dict): # проверяем, что элемент прикреплен к DOM
        element = self.get_locator(element_dict)
        expect(element).to_be_enabled()
        print(f"{element_dict.get('description')} enabled")

    def check_element_has_text(self, element_dict: dict, expected_text: str): # проверяем, что элемент содержит текст
        element = self.get_locator(element_dict)
        expect(element).to_have_text(expected_text)
        print(f"{element_dict.get('description')} has text: {expected_text}")

    def check_element_is_readonly(self, element_dict: dict): # проверяем, что элемент кликабелен
        element = self.get_locator(element_dict)
        expect(element).to_be_editable()
        print(f"{element_dict.get('description')} enabled")