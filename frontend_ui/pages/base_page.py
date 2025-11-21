
from playwright.sync_api import Page, expect


class BasePage:

    url = None
    def __init__(self, page: Page):
        self.page = page

    def open(self):
        if self.url:
            self.page.goto(self.url)

    def check_element_visible(self, selector: str, element_name: str): # проверяем, что элемент видим
        element = self.page.locator(selector)
        expect(element).to_be_visible()
        print(f"{element_name} visible")

    def check_element_attached(self, selector: str, element_name: str): # проверяем, что элемент прикреплен к DOM
        element = self.page.locator(selector)
        expect(element).to_be_attached()
        print(f"{element_name} attached DOM")

    def check_element_has_text_is_(self, selector: str, expected_text: str, element_name: str): # проверяем, что элемент содержит текст
        element = self.page.locator(selector)
        expect(element).to_have_text(expected_text)
        print(f"{element_name} has text: {expected_text}")