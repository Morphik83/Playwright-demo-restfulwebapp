"""
Basic example script for automating https://automationintesting.online/ with Playwright
This script demonstrates the most basic interactions with the website.
"""

from playwright.sync_api import sync_playwright 

def main():
  
    with sync_playwright() as playwright:
        # Launch the browser with headed mode (visible) and slower actions for visibility
        browser = playwright.chromium.launch(headless=False, slow_mo=500)
        page = browser.new_page(viewport={"width": 1280, "height": 720})
        page.goto("https://automationintesting.online/")
        
        # Add a small delay to see the page
        page.wait_for_timeout(3000)
        
        # Close the browser inside the context manager
        browser.close()

if __name__ == "__main__":
    main()
