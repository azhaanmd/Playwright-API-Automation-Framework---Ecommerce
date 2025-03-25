from playwright.sync_api import Playwright, expect
from utils.apiBase import APIUtils
from pageObjects.login import LoginPage
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
def test_e2e_web_api(playwright:Playwright, userCredentials, browserInstance):
    user_email = userCredentials["userEmail"]
    user_password = userCredentials["userPassword"]

    print(f'Using User:: {user_email}\n')
    #print(f'Test User No: {userTestCount}\n')
    #userTestCount+=1
    
    #--------------API PART-------------------
    #create order -> orderID ::
    api_utils = APIUtils()
    orderID = api_utils.createOrder(playwright, userCredentials)

    #--------------UI PART-------------------
    #login
    loginPage = LoginPage(browserInstance) #browserInstance is returning page object 
    loginPage.navigate()
    dashboardPage = loginPage.login(user_email, user_password)

    #dashboard
    # dashboardPage = DashboardPage(page)
    orderHistoryPage = dashboardPage.selectOrdersNavigationLink()
    orderDetailPage = orderHistoryPage.selectOrder(orderID)

    orderDetailPage.verifyOrderMessage()


    #orders history page -> order is present
