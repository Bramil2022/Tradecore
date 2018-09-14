from page_objects import PageElement, PageObject
from selenium.webdriver.common.by import By
from selenium import webdriver
from pages.base_page import BasePage
from selenium.webdriver.common.keys import Keys
from locators.registration_page_locators import RegistrationPageLocators
from pages.registration_page_step2 import RegistrationStep2Page
import time
from selenium.webdriver.support.ui import Select
from pages.homepage import Homepage
from property import Property


class RegistrationPage(BasePage):
    """Registration page of TradeCore"""

    def wait_for_registration_page_load(self):
        self.wait_for_page_load((RegistrationPageLocators.FIRST_NAME_FIELD), 25)
        time.sleep(1)
        return self

    def type_first_name(self, first_name):
        self.wait_for_element_to_be_clickable((RegistrationPageLocators.FIRST_NAME_FIELD), 5)
        element = self._driver.find_element(*RegistrationPageLocators.FIRST_NAME_FIELD)
        element.send_keys(first_name)
        return self

    def type_last_name(self, last_name):
        element = self._driver.find_element(*RegistrationPageLocators.LAST_NAME_FIELD)
        element.clear()
        element.send_keys(last_name)
        return self

    def type_email(self, email):
        element = self._driver.find_element(*RegistrationPageLocators.EMAIL_FIELD)
        element.clear()
        element.send_keys(email)
        return self

    def type_password(self, password):
        element = self._driver.find_element(*RegistrationPageLocators.PASSWORD_FIELD)
        element.clear()
        element.send_keys(password)
        return self

    def type_phone(self, phone):
        element = self._driver.find_element(*RegistrationPageLocators.PHONE_FIELD)
        element.send_keys(phone)
        return self

    def type_date_of_birth(self, date_of_birth):
        self.wait_for_element_to_be_clickable((RegistrationPageLocators.DATE_OF_BIRTH_FIELD), 5)
        element = self._driver.find_element(*RegistrationPageLocators.DATE_OF_BIRTH_FIELD)
        element.send_keys(date_of_birth)
        return self

    def type_postcode(self, postcode):
        element = self._driver.find_element(*RegistrationPageLocators.POSTCODE_FIELD)
        element.send_keys(postcode)
        return self

    def type_address1(self, address):
        element = self._driver.find_element(*RegistrationPageLocators.ADDRESS1_FIELD)
        element.send_keys(address)
        return self

    def type_city(self, city):
        element = self._driver.find_element(*RegistrationPageLocators.CITY_FIELD)
        element.send_keys(city)
        return self

    def click_next_button(self):
        element = self._driver.find_element(*RegistrationPageLocators.NEXT_BUTTON)
        element.click()
        return RegistrationStep2Page(self._driver)

    def register_user(self):
        '''Method for simple user registration (fills only required fields)'''

        '''Filling step 1 registration fields'''
        registration_page = RegistrationPage(self._driver).wait_for_registration_page_load() \
            .type_first_name(Property.FIRST_NAME).type_last_name(Property.LAST_NAME) \
            .type_email(Property.EMAIL).type_password(Property.PASSWORD) \
            .type_phone(Property.PHONE).type_date_of_birth(Property.DATE_OF_BIRTH) \
            .type_postcode(Property.POSTCODE).type_address1(Property.ADDRESS1).type_city(Property.CITY)
        '''Filling step 2 registration fields'''
        registration_step2_page = registration_page.click_next_button().wait_for_registration_page_step2_to_laod() \
            .select_shares(Property.SHARES).select_forex(Property.FOREX)\
            .select_cfds(Property.CFDS).select_spread_betting(Property.SPREAD_BETTING)\
            .select_relevent_experience(Property.FINANCIAL_SECTOR_EXPERIENCE)
        registration_step2_page.scroll_to_bottom_of_the_page()
        registration_step2_page\
            .select_trading_platform().select_trading_currency(Property.CURRENCY)\
            .select_annual_income(Property.APPROX_ANNUAL_INCOME).select_employment_status(Property.EMPOLYMENT_STATUS)\
            .select_value_of_assets(Property.APPROX_VALUE_OF_ASSETS)\
            .check_i_have_read()
        '''Accepting terms from policy update'''
        policy_popup = registration_step2_page.click_finish_button()\
            .wait_for_policy_popup_load()\
            .click_agree_button()
        return Homepage(self._driver)

    def get_number_of_reqired_field_messages(self):
        reqired_field_message_locators = self._driver.find_elements(*RegistrationPageLocators.REQUIRED_FIELD)
        return len(reqired_field_message_locator)