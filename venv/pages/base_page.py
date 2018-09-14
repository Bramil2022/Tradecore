from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


class BasePage(object):
    _driver = None

    def __init__(self, driver):
        self._driver = driver

    def wait_for_page_load(self, element_identifier, time):
        wait = WebDriverWait(self._driver, time)
        wait.until(EC.presence_of_element_located((element_identifier)))


    def wait_for_element_to_be_clickable(self, element, time):
        wait = WebDriverWait(self._driver, time)
        wait.until(EC.element_to_be_clickable((element)))

    def select_option_by_name_from_dropdown(self, option_name, dropdown_locator):
        select = Select(self._driver.find_element(*dropdown_locator))
        select.select_by_visible_text(option_name)

    def scroll_to_bottom_of_the_page(self):
        self._driver.find_element(By.CSS_SELECTOR, 'body').send_keys(Keys.PAGE_DOWN)
        time.sleep(1)

    '''
    Gets user full name from top right corner
    @return user full name
    '''
    def get_user_fullname_from_topbar(self):
        users_fullname = self._driver.find_element(By.XPATH, "//div[@ng-show = 'data.isLogged']").text
        users_fullname = users_fullname[0:-8] #substring [Logout]
        return users_fullname

    def get_title(self):
        title = self._driver.title
        return title


