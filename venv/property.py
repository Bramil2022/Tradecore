from utils.date_time_utils import DateTimeUtils
from selenium import webdriver


class Property():
    """User property"""

    '''Drivers'''
    CHROME = webdriver.Chrome(r'Drivers\chromedriver.exe')

    '''URLs'''
    TRADECORE_REGISTRATION_FROM_URL = 'https://demo-biq.dev.tradecore.io/#/'


    '''First step registration content'''
    FIRST_NAME = 'Branislav'
    LAST_NAME = 'Milutinovic'
    EMAIL = 'bane+'+str(DateTimeUtils().get_timestamp())+'@tradecore.com'
    PASSWORD = 'Tradecore1!'
    PHONE = '611169216'
    DATE_OF_BIRTH = '22 02 1991'
    COUNTRY = 'Serbia'
    POSTCODE = '11000'
    ADDRESS1 = '325 Park St'
    CITY = 'Belgrade'

    '''Second step registration content'''
    SHARES = "no"                            # frequently/sometimes/no
    FOREX = 'sometimes'                      # frequently/sometimes/no
    CFDS = "frequently"                      # frequently/sometimes/no
    SPREAD_BETTING = "no"                    # frequently/sometimes/no
    FINANCIAL_SECTOR_EXPERIENCE = 'course'   # course/work/no
    CURRENCY = 'USD'                         # USD/EUR/GBP
    APPROX_ANNUAL_INCOME = 'medium'          # very high/high/medium/low
    EMPOLYMENT_STATUS = 'employed'           # employed/self employed/retired/student/unemployed
    APPROX_VALUE_OF_ASSETS = 'low'           # very high/high/medium/low
