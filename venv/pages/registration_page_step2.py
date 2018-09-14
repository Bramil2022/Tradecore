from page_objects import PageElement, PageObject
from selenium.webdriver.common.by import By
from selenium import webdriver
from pages.base_page import BasePage
from selenium.webdriver.common.keys import Keys
from locators.registration_page_step2_locators import RegistrationPageStep2Locators
import time
from selenium.webdriver.support.ui import Select
from pages.containers.policy_popup import PolicyPopup


class RegistrationStep2Page(BasePage):
    """Registration page of TradeCore step 2"""



    def wait_for_registration_page_step2_to_laod(self):
        self.wait_for_page_load((RegistrationPageStep2Locators.I_HAVE_READ_CHECKBOX), 25)
        time.sleep(1)
        return self

    '''
    Choses option from Shares dropdown
    @param string option     3 options: no/sometimes/frequently
    @return string formatted string
    '''
    def select_shares(self, option):
        self._first_four_dropdowns_util(option, RegistrationPageStep2Locators.SHARES_DROPDOWN)
        return self

    def select_forex(self, option):
        self._first_four_dropdowns_util(option, RegistrationPageStep2Locators.FOREX_DROPDOWN)
        return self

    def select_cfds(self, option):
        self._first_four_dropdowns_util(option, RegistrationPageStep2Locators.CFDS_DROPDOWN)
        return self

    def select_spread_betting(self, option):
        self._first_four_dropdowns_util(option, RegistrationPageStep2Locators.SPREAD_BETTING_DROPDOWN)
        return self

    '''
    Select relevent experience in financial sector
    @param option course/work or if anything else is but it will select no experience
    '''
    def select_relevent_experience(self, option):
        dropdown = self._driver.find_element(*RegistrationPageStep2Locators.HAVE_YOU_DROPDOWN)
        dropdown.click()
        if (option is 'course'):
            element_option = dropdown.find_element(By.CSS_SELECTOR, 'ul li:nth-child(1)')
        elif (option is 'work'):
            element_option = dropdown.find_element(By.CSS_SELECTOR, 'ul li:nth-child(2)')
        else:
            element_option = dropdown.find_element(By.CSS_SELECTOR, 'ul li:nth-child(3)')
        element_option.click()
        return self


    def select_trading_platform(self):
        dropdown = self._driver.find_element(*RegistrationPageStep2Locators.TRADING_PLATFORM_DROPDOWN)
        dropdown.click()
        element_option = dropdown.find_element(By.CSS_SELECTOR, 'ul li:nth-child(1)') #TODO there is only one option
                                                                                        # put more once more are added
        element_option.click()
        return self

    def select_trading_currency(self, option):
        dropdown = self._driver.find_element(*RegistrationPageStep2Locators.TRADING_CURRENCY_DROPDOWN)
        dropdown.click()
        if (option is 'USD'):
            element_option = dropdown.find_element(By.CSS_SELECTOR, 'ul li:nth-child(1)')
        elif (option is 'EUR'):
            element_option = dropdown.find_element(By.CSS_SELECTOR, 'ul li:nth-child(2)')
        elif (option is 'GBP'):
            element_option = dropdown.find_element(By.CSS_SELECTOR, 'ul li:nth-child(3)')
        element_option.click()
        return self


    def select_annual_income(self, option):
        dropdown = self._driver.find_element(*RegistrationPageStep2Locators.APPROX_ANNUAL_INCOME_DROPDOWN)
        dropdown.click()
        if (option is 'very high'):
            element_option = dropdown.find_element(By.CSS_SELECTOR, 'ul li:nth-child(1)')
        elif (option is 'high'):
            element_option = dropdown.find_element(By.CSS_SELECTOR, 'ul li:nth-child(2)')
        elif (option is 'medium'):
            element_option = dropdown.find_element(By.CSS_SELECTOR, 'ul li:nth-child(3)')
        elif (option is 'low'):
            element_option = dropdown.find_element(By.CSS_SELECTOR, 'ul li:nth-child(4)')
        element_option.click()
        return self

    def select_employment_status(self, option):
        dropdown = self._driver.find_element(*RegistrationPageStep2Locators.EMPOLYMENT_STATUS_DROPDOWN)
        dropdown.click()
        if (option is 'employed'):
            element_option = dropdown.find_element(By.CSS_SELECTOR, 'ul li:nth-child(1)')
        elif (option is 'self employed'):
            element_option = dropdown.find_element(By.CSS_SELECTOR, 'ul li:nth-child(2)')
        elif (option is 'retired'):
            element_option = dropdown.find_element(By.CSS_SELECTOR, 'ul li:nth-child(3)')
        elif (option is 'student'):
            element_option = dropdown.find_element(By.CSS_SELECTOR, 'ul li:nth-child(4)')
        elif (option is 'unemployed'):
            element_option = dropdown.find_element(By.CSS_SELECTOR, 'ul li:nth-child(5)')
        element_option.click()
        return self

    def select_value_of_assets(self, option):
        dropdown = self._driver.find_element(*RegistrationPageStep2Locators.APPROX_VALUE_OF_ASSETS_DROPDOWN)
        dropdown.click()
        if (option is 'very high'):
            element_option = dropdown.find_element(By.CSS_SELECTOR, 'ul li:nth-child(1)')
        elif (option is 'high'):
            element_option = dropdown.find_element(By.CSS_SELECTOR, 'ul li:nth-child(2)')
        elif (option is 'medium'):
            element_option = dropdown.find_element(By.CSS_SELECTOR, 'ul li:nth-child(3)')
        elif (option == 'low'):
            element_option = dropdown.find_element(By.CSS_SELECTOR, 'ul li:nth-child(4)')
        element_option.click()
        return self

    def check_i_have_read(self):
        element = self._driver.find_element(*RegistrationPageStep2Locators.I_HAVE_READ_CHECKBOX)
        element.click()
        return self

    def click_finish_button(self):
        element = self._driver.find_element(*RegistrationPageStep2Locators.FINISH_BUTTON)
        element.click()
        return PolicyPopup(self._driver)

    '''
    Private method that handels options for first 4 dropdowns
    @param string option     3 options: no/sometimes/frequently
    @param locator of dropdown
    '''
    def _first_four_dropdowns_util(self, option, dropdown_locator):
        dropdown = self._driver.find_element(*dropdown_locator)
        dropdown.click()
        if (option is 'frequently'):
            element_option = dropdown.find_element(By.CSS_SELECTOR, 'ul li:nth-child(1)')
        elif (option is 'sometimes'):
            element_option = dropdown.find_element(By.CSS_SELECTOR, 'ul li:nth-child(2)')
        else:
            element_option = dropdown.find_element(By.CSS_SELECTOR, 'ul li:nth-child(3)')
        element_option.click()

    def get_number_of_reqired_field_messages(self):
        reqired_field_message_locators = self._driver.find_elements(*RegistrationPageStep2Locators.REQUIRED_FIELD)
        return len(reqired_field_message_locators)