from pages.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.username = page.locator("#username")
        self.password = page.locator("#password")
        self.login_button = page.locator("#login-btn")
        self.login_message = page.locator("#message")

    def open(self):
        self.page.goto("file:///I:/sneha/Development/PlaywrightFramework/login.html")
        self.wait_for_page_load()

    def login(self, username, password):
        self.username.fill(username)
        self.password.fill(password)
        self.login_button.click()
        self.wait_for_page_load()
