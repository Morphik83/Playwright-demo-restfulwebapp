# Page object: home page 
from pages.base_page import BasePage

class HomePage(BasePage):
    """Home page object model for the Restful-Booker Platform"""

    def __init__(self, page):
        """Initialize parent class and define locators"""
        super().__init__(page)

    # Interaction methods
    def fill_username(self, name):
        self.page.get_by_test_id("ContactName").fill(name)

    def fill_email(self, email):
        self.page.get_by_test_id("ContactEmail").fill(email)

    def fill_phone(self, phone):
        self.page.get_by_test_id("ContactPhone").fill(phone)

    def fill_subject(self, subject):
        self.page.get_by_test_id("ContactSubject").fill(subject)

    def fill_message(self, msg):
        self.page.get_by_test_id("ContactDescription").fill(msg)

    def submit_form(self):
        """Submit the contact form by clicking the submit button"""
        self.page.get_by_role("button", name="Submit").click()

    # Business-level methods
    def fill_contact_form(self, name, email, phone, subject, message):
        """
        Fill out contact form

        Args:
            name: Customer name to enter in the form
            email: Customer email to enter in the form
            phone: Customer phone to enter in the form
            subject: Subject of the message to enter in the form
            message: Message to enter in the form
        """

        # Wait for the page to load
        self.wait_for_the_page_to_load()

        # Fill in the form fields with small delay for stability
        self.fill_username(name)
        self.page.wait_for_timeout(200)

        self.fill_email(email)
        self.page.wait_for_timeout(200)

        self.fill_phone(phone)
        self.page.wait_for_timeout(200)

        self.fill_subject(subject)    
        self.page.wait_for_timeout(200)

        self.fill_message(message)
        self.page.wait_for_timeout(200)