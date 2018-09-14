from pages.base_page import BasePage
from locators.containers.policy_popup_locators import PolicyPopupLocators
from pages.homepage import Homepage
import time

class PolicyPopup(BasePage):
    """Policy update pop up"""


    def wait_for_policy_popup_load(self):
        time.sleep(1)
        self.wait_for_page_load((PolicyPopupLocators.AGREE_BUTTON), 60)
        return self

    def click_agree_button(self):
        agree_button = self._driver.find_element(*PolicyPopupLocators.AGREE_BUTTON)
        agree_button.click()
        return Homepage(self._driver)