from pages.base_page import BasePage


class DashboardPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.welcome_message = page.locator("#welcome-message")
        self.profile_button = page.locator("#profile-btn")
        self.logout_button = page.locator("#logout-btn")

    def logout(self):
        self.logout_button.click()
        self.wait_for_page_load()

    def go_to_profile(self):
        self.profile_button.click()
        self.wait_for_page_load()
