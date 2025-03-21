from playwright.sync_api import Playwright, expect
from utils.apiBase import APIUtils

def test_e2e_web_api(playwright:Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    #json file -> utils ->

    #create order -> orderID
    api_utils = APIUtils()
    orderID = api_utils.createOrder(playwright)

    #login
    page.goto("https://rahulshettyacademy.com/client/")
    page.get_by_placeholder("email@example.com").fill("rahulshetty@gmail.com")
    page.get_by_placeholder("enter your passsword").fill("Iamking@000")
    page.get_by_role("button", name="Login").click()


    #orders history page -> order is present
    page.get_by_role("button", name="ORDERS").click()
    orderRow = page.locator("tr").filter(has_text=orderID)
    orderRow.get_by_role("button", name = "View").click()
    expect(page.locator(".tagline")).to_contain_text("Thank you")