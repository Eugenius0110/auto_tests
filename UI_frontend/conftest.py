import pytest
from playwright.sync_api import Page, expect


@pytest.fixture()
def page(context):
    page: Page = context.new_page()
    page.set_viewport_size({'height': 800, 'width': 1000})
    yield page



