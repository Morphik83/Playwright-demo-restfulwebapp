import unittest
from playwright.sync_api import sync_playwright

class TestHomePageTitle(unittest.TestCase):
    def test_home_page_title(self):
        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page()
            page.goto("https://example.com")
            self.assertIn("Example Domain", page.title())
            browser.close()

if __name__ == "__main__":
    unittest.main()
