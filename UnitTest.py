# coding=utf-8
__author__ = 'lucas.arana'

import unittest
from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class UnitTesting(unittest.TestCase):
    """
    Made this class because
    i was bored of doing it manually
    """

    def setUp(self):
        self.browser = webdriver.Firefox()
        # Uncomment for chrome testing (note: you'll have to change the path to your chrome driver)
        # self.browser = webdriver.Chrome('C:\Users\lucas.arana\Downloads\chromedriver')

    def tearDown(self):
        """
        Comment this function if
        you don't want to close the Browser after finished
        """
        self.browser.close()

    def test_code_petition_with_login(self):
        self.browser.get('http://localhost:2020/petition')

        try:
            WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.ID, "authorize")))
        finally:
            user_element = self.browser.find_element_by_id('username')
            pass_element = self.browser.find_element_by_id('password')
            user = "arana_lucas@hotmail.com"
            password = "testeando"

            user_element.send_keys(user)
            pass_element.send_keys(password)
            authorize_app = self.browser.find_element_by_id('authorize')
            authorize_app.click()
        try:
            WebDriverWait(self.browser, 10).until(EC.visibility_of("ok"))
        finally:
            bodyText = self.browser.find_element_by_tag_name('body').text
            assert 'error' not in bodyText

    def test_ask_user(self):
        self.browser.get('http://localhost:2020/get_sound_cloud_user?user_id=user495277334')
        bodyText = self.browser.find_element_by_tag_name('body').text
        assert 'error' not in bodyText


if __name__ == '__main__':
    unittest.main()
