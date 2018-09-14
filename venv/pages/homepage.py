from pages.base_page import BasePage
from locators.homepage_locators import HomepageLocators


class Homepage(BasePage):
    """Main page where user logs in/signs up"""


    def wait_for_homepage_to_load(self):
        self.wait_for_page_load((HomepageLocators.HOMEPAGE_HEADING), 25)
        time.sleep(1)
        return self


