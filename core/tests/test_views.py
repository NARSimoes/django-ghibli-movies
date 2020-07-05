
import logging

from django.test import LiveServerTestCase
from selenium.webdriver.common.keys import Keys
import unittest
from selenium import webdriver

logger = logging.getLogger(__name__)


try:
    # simple check for firefox in system, if not exists
    # we just want non graphical tests....
    browser = webdriver.Firefox(
        executable_path='/usr/src/geo_exercise/geckodriver'
    )

    # yeah, we have firefox, lets test.
    class AccountTestCase(LiveServerTestCase):
        """Test user register using selenium is required geckodriver."""
        databases = {'default'}

        def setUp(self):
            self.selenium = webdriver.Firefox(
                executable_path='/ghiblimovies/geckodriver'
            )
            super(AccountTestCase, self).setUp()

        def tearDown(self):
            self.selenium.quit()
            super(AccountTestCase, self).tearDown()

        def test_register(self):
            selenium = self.selenium
            # Opening the link we want to test
            selenium.get('http://127.0.0.1:8990/accounts/signup/')
            # find the form element
            username = selenium.find_element_by_id('id_username')
            email = selenium.find_element_by_id('id_email')
            password1 = selenium.find_element_by_id('id_password1')
            password2 = selenium.find_element_by_id('id_password2')

            submit = selenium.find_element_by_name('signup')

            # Fill the form with data
            username.send_keys('Teste')
            email.send_keys('test@cenas.com')
            password1.send_keys('123456')
            password2.send_keys('123456')

            # submitting the form
            submit.send_keys(Keys.RETURN)

            # check the returned result
            assert 'Check your email' in selenium.page_source

    class TestSignup(unittest.TestCase):
        """Test user register is required geckodriver."""
        databases = {'default'}

        def setUp(self):
            self.driver = webdriver.Firefox(
                executable_path='/ghiblimovies/geckodriver'
            )

        def test_signup_fire(self):
            self.driver.get("http://localhost:8990/accounts/signup/")
            self.driver.find_element_by_id('id_mail').send_keys("a@mail.com")
            self.driver.find_element_by_id('id_user').send_keys("test_user")
            self.driver.find_element_by_id('id_pass1').send_keys("test_pass")
            self.driver.find_element_by_id('id_pass2').send_keys("test_pass")
            self.driver.find_element_by_id('signup').click()
            self.assertIn("http://127.0.0.1:8990/", self.driver.current_url)

        def tearDown(self):
            self.driver.quit

except Exception as e:
    logger.debug(
        "Firefox isn't installed.\
         Do you want execute just non graphical tests?", e
    )
