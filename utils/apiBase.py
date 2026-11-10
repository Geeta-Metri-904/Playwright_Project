from playwright.sync_api import Playwright

orders_payload = {"orders":[{"country":"India","productOrderedId":"6960eac0c941646b7a8b3e68"}]}

class APIUtils:

    def get_token(self,playwright:Playwright):
        api_new_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com")
        response = api_new_context.post("/api/ecom/auth/login",
                             data = {"userEmail":"geetametri904@gmail.com","userPassword":"Geeta123$"})
        assert response.ok
        print(response.json())
        response_body = response.json()
        return response_body["token"]

    def create_order(self,playwright:Playwright):
        token = self.get_token(playwright)
        api_new_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com")
        response = api_new_context.post("/api/ecom/order/create-order",
                             data = orders_payload,
                             headers = {"Authorization" : token,
                                        "Content-Type": "application/json"
                                        })
        print(response.json())
        response_body = response.json()
        order_id = response_body["orders"][0]
        return order_id
