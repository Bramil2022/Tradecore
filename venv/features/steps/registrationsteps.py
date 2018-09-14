from behave import given, when, then
from selenium import webdriver
from pages.registration_page import RegistrationPage
import time
from property import Property
from pages.registration_page_step2 import RegistrationStep2Page
from pages.homepage import Homepage
from pages.containers.policy_popup import PolicyPopup
from data.data_en import Data

driver = None


@given(u'registration page')
def step_impl(context):
    driver = Property.CHROME
    driver.maximize_window()
    driver.get(Property.TRADECORE_REGISTRATION_FROM_URL)
    context.driver = driver


@when(u'fill correctly all required fields')
def step_impl(context):
    registration_page = RegistrationPage(context.driver)
    registration_page.register_user()


@then(u'user is successfully registrated')
def step_impl(context):
    """Verifications"""

    """Verify that user is on homepage"""
    homepage = Homepage(context.driver)
    expected_title = Data.HOMEPAGE_TITLE
    actual_title = homepage.get_title()
    assert expected_title == actual_title, "Wrong title! Got: %r" % actual_title

    """Verify that newly registrated user is logged"""
    expected_user_fullname = Property.FIRST_NAME + ' ' + Property.LAST_NAME
    actual_user_fullname = homepage.get_user_fullname_from_topbar()
    assert expected_user_fullname == actual_user_fullname, "Wrong fullname! Got: %r" % actual_user_fullname
    context.driver.quit()




@given(u'starting registration page')
def step_impl(context): # TODO fix this test to work when run with first also, not only individualy
    driver = Property.CHROME
    driver.maximize_window()
    driver.get(Property.TRADECORE_REGISTRATION_FROM_URL)
    context.driver = driver

@when(u'just click next button without filling any field')
def step_impl(context):
    context.registration_page = RegistrationPage(context.driver).wait_for_registration_page_load()\
        .click_next_button()


@then(u'user can\'t proceed to step 2')
def step_impl(context):
    """Verification"""

    """Verify that user stays on registration step 1 page"""
    expected_title = Data.REGISTRATION_PAGE_STEP1_TITLE
    actual_title = context.registration_page.get_title()
    assert expected_title == actual_title, "Wrong title! Got: %r" % actual_title


@then(u'info/error message are written below required fields')
def step_impl(context):
    total_number_of_required_fields = 9
    number_of_field_required_messages = context.registration_page.get_number_of_reqired_field_messages()
    """Verify that there are info/error message for each required field"""
    assert total_number_of_required_fields == number_of_field_required_messages, "Wrong! Expected 9, Got: %r" % number_of_field_required_messages
    context.driver.quit()


#TODO this test
@given(u'starting with registration page')
def step_impl(context):
    pass


@when(u'fill password field with \'<invalid password>\'')
def step_impl(context):
    pass

@then(u'verify that user got info/error message about invalid password')
def step_impl(context):
    pass
