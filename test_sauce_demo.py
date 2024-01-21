import unittest
import logging
from configparser import ConfigParser
from selenium import webdriver
from selenium.webdriver.common.by import By

import sauce_scratch

r = ConfigParser()
r.read('config.ini')
logging.basicConfig(filename='../AutomationTesting_Learning000/logs/test_sauce_demo.log',
                    format='%(asctime)s %(levelname)s: %(message)s', filemode='w',
                    encoding='utf-8-sig', level=logging.INFO, force=True)


class TestSauceDemo(unittest.TestCase):
    driver = webdriver.Chrome()

    @classmethod
    def setUpClass(cls):
        cls.driver.maximize_window()
        cls.driver.get(r['url']['saucedemo'])
        swag_scratch.verify_element_login(cls)

    def setUp(self):
        """Can be used for pre-requisite steps"""
        swag_scratch.login(self)
        swag_scratch.check_footer(self)
        swag_scratch.check_menu(self)
        swag_scratch.check_inventories(self)
        swag_scratch.choose_products(self)
        swag_scratch.open_cart(self)

    def tearDown(self):
        swag_scratch.logout(self)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_a_shopping(self):
        swag_scratch.address_filling(self)
        swag_scratch.payment_confirmation(self)
        swag_scratch.thank_you(self)
        logging.info('Shopping test is succeed')

    def test_b_blank_filling(self):
        """empty form"""
        self.driver.find_element(By.ID, 'continue').click()
        self.driver.find_element(By.XPATH, "//h3[normalize-space()"
                                           "='Error: First Name is required']").is_displayed()
        logging.info('Blank address filling test is succeed')


if __name__ == "__main__":
    unittest.main()
