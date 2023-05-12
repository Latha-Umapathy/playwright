from playwright.sync_api import Playwright, sync_playwright, expect

from petstore.page_object.home_page_elements import homepage
import pytest


@pytest.mark.smoke
@pytest.mark.regression
def test_sign_in(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=True, slow_mo=500)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://petstore.octoperf.com/actions/Catalog.action")
    home_page = homepage(page)
    home_page.sign_in_link.click()
    expect(home_page.username).to_be_visible()
    context.close()
    browser.close()

@pytest.mark.integration
def test_reptiles(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=True, slow_mo=500)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://petstore.octoperf.com/actions/Catalog.action")
    home_page = homepage(page)
    home_page.reptiles_link.click()
    expect(home_page.reptiles_header).to_be_visible()
    context.close()
    browser.close()
