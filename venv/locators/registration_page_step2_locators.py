from selenium.webdriver.common.by import By


class RegistrationPageStep2Locators(object):
    """A class for registration page step 2 locators."""
    SHARES_DROPDOWN = (By.XPATH, "//div[@field-id = 'shares']")
    FOREX_DROPDOWN = (By.XPATH, "//div[@field-id = 'forex']")
    CFDS_DROPDOWN = (By.XPATH, "//div[@field-id = 'cfds']")
    SPREAD_BETTING_DROPDOWN = (By.XPATH, "//div[@field-id = 'spread_betting']")
    I_HAVE_READ_CHECKBOX = (By.CSS_SELECTOR, "label.checkbox")
    HAVE_YOU_DROPDOWN = (By.XPATH, "//div[@field-id = 'relevant_experience']")
    TRADING_PLATFORM_DROPDOWN = (By.XPATH, "//div[@field-id = 'trading_accounts']")
    TRADING_CURRENCY_DROPDOWN = (By.XPATH, "//div[@field-id = 'currency']")
    APPROX_ANNUAL_INCOME_DROPDOWN = (By.XPATH, "//div[@field-id = 'approx_annual_income']")
    EMPOLYMENT_STATUS_DROPDOWN = (By.XPATH, "//div[@field-id = 'employment_status']")
    APPROX_VALUE_OF_ASSETS_DROPDOWN = (By.XPATH, "//div[@field-id = 'liquid_savings']")
    FINISH_BUTTON = (By.ID, 'button-step')
    REQUIRED_FIELD = (By.XPATH, "//div[@ng-message = 'required']")