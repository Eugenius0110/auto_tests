from playwright.sync_api import Page, expect, Dialog, BrowserContext


# def test_wiki(page: Page):
#     page.goto('https://www.wikipedia.org/')
#     page.get_by_role('link', name='Русский').click()
#     expect(page.get_by_text('Добро пожаловать в Википедию')).to_be_visible()
#
# def test_wiki2(page: Page):
#     page.goto('https://www.wikipedia.org/')
#     page.get_by_role('link', name='Русский').click()
#     page.get_by_role('link', name='Содержание').click()
#     page.locator('#ca-talk').click()
#     expect(page.locator('#firstHeading')).to_have_text('Обсуждение Википедии:Содержание')

# def test_alerts(page: Page):
#     page.goto('https://demoblaze.com/')
#
#     def accept_alert(alert: Dialog):
#         print(alert.message)
#         alert.accept()
#
#     page.on('dialog', accept_alert) # когда, в случае если
#     page.get_by_role('link', name='Samsung galaxy s6').click()
#     page.get_by_role('link', name='Add to cart').click()
#     page.locator('#cartur').click() # поиск по id, '.cartur' поиск по class

def test_tabs(page: Page, context: BrowserContext):
    page.goto('https://nomadlist.com/')
    with context.expect_page() as new_tab_event:
        page.get_by_alt_text('Get insured').click()
        new_tab = new_tab_event.value
    new_tab.get_by_role('button', name='sign me up').click()

def test_select(page: Page):
    page.goto('https://semantic-ui.com/modules/dropdown.html')
    page.get_by_role('link', name='Search Selection').click()