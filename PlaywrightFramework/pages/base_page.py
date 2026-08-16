class BasePage:
    def __init__(self, page):
        self.page = page

    def wait_for_page_load(self):
        self.page.wait_for_load_state("networkidle")

    def expect_url(self, expected_url):
        assert self.page.url == expected_url
