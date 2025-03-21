from playwright.sync_api import Playwright

ordersPayload = {"orders": [{"country": "Bangladesh", "productOrderedId": "67a8df1ac0d3e6622a297ccb"}]}

class APIUtils:

    def getToken(self, playwright:Playwright):
        api_request_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com/")
        response = api_request_context.post("api/ecom/auth/login",
                                            data = {"userEmail": "rahulshetty@gmail.com", "userPassword": "Iamking@000"})
        assert response.ok
        responseBody = response.json()
        return responseBody["token"]

    def createOrder(self, playwright:Playwright):
        token = self.getToken(playwright) #self -> because it is from same class
        api_request_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com/")
        response = api_request_context.post("api/ecom/order/create-order",
                                 data=ordersPayload, 
                                 headers={"Authorization": token, 
                                          "Content-Type": "application/json"})
        print(response.json())
        responseBody = response.json()
        return responseBody["orders"][0]