from playwright.sync_api import Playwright, expect
from utils.apiBase import APIUtils
import json, os, pytest

#userTestCount = int(1)
file_path = "Playwright/data/credentials.json"
#json file -> utils ->
# Open and read the file
with open(file_path) as f:
    test_data = json.load(f)
    #print(test_data)
user_credentials_list = test_data['user_credentials']


@pytest.mark.parametrize('userCredentials', user_credentials_list) #pulls one item each time to execute using that data
def test_e2e_web_api(playwright:Playwright, userCredentials):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    #create order -> orderID
    api_utils = APIUtils()
    orderID = api_utils.createOrder(playwright, userCredentials)

    #login
    page.goto("https://rahulshettyacademy.com/client/")
    page.get_by_placeholder("email@example.com").fill(userCredentials["userEmail"])
    page.get_by_placeholder("enter your passsword").fill(userCredentials["userPassword"])
    page.get_by_role("button", name="Login").click()
    print(f'Using User:: {userCredentials["userEmail"]}\n')
    #print(f'Test User No: {userTestCount}\n')
    #userTestCount+=1


    #orders history page -> order is present
    page.get_by_role("button", name="ORDERS").click()
    orderRow = page.locator("tr").filter(has_text=orderID)
    orderRow.get_by_role("button", name = "View").click()
    expect(page.locator(".tagline")).to_contain_text("Thank you")