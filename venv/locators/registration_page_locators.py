from selenium.webdriver.common.by import By

class RegistrationPageLocators(object):
    """A class for registration page locators."""
    FIRST_NAME_FIELD = (By.ID, 'form-first_name')
    LAST_NAME_FIELD = (By.ID, 'form-last_name')
    EMAIL_FIELD = (By.ID, 'form-email')
    PASSWORD_FIELD = (By.ID, 'form-password')
    PHONE_FIELD = (By.ID, "form-telephone")
    DATE_OF_BIRTH_FIELD = (By.ID, 'form-date_of_birth')
    COUNTRY_DROPDOWN_FIELD = (By.ID, 'form___fieldId___chosen')
    POSTCODE_FIELD = (By.ID, 'form-addr_zip')
    ADDRESS1_FIELD = (By.ID, 'form-addr_street')
    CITY_FIELD = (By.ID, 'form-addr_city')
    NEXT_BUTTON = (By.ID, 'button-step')
    REQUIRED_FIELD = (By.XPATH, "//div[@ng-message = 'required']")
