# Base page with common functionality

class BasePage:
    """Base page object that all page objects will inherit from"""

    def __init__(self, page):
        """
        Initialize the base page

        Args:
            page: Playwright page object
        """
        self.page = page 
        self.base_url = "https://automationintesting.online"

    def navigate_to(self, path=""):
        """
        Navigate to the specific path on the website

        Args:
            path: The path to navigate to (append to base_url)
        """
        self.page.goto(f"{self.base_url}/{path}")

    def wait_for_the_page_to_load(self):
        """Wait for the page to be fully loaded"""
        self.page.wait_for_load_state("networkidle")
        

