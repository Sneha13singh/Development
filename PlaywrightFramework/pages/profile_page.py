class ProfilePage:
    def __init__(self, page):
        self.page = page
        self.profile_heading = page.locator("#profile-heading")
        self.dashboard_button = page.locator("#dashboard-btn")

    def go_to_dashboard(self):
        self.dashboard_button.click()
        self.page.wait_for_load_state("networkidle")
