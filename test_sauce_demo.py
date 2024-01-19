import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as ec
import time
import logging
from configparser import ConfigParser

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
        cls.driver.get(r['basic info']['saucedemo'])
        title = cls.driver.title
        assert "Swag Labs" in title

    def setUp(self):
        """Can be used for pre-requisite steps"""
        """input correct username and password"""
        self.driver.find_element(By.ID, 'user-name').send_keys(r['user']['swag_id'])
        self.driver.find_element(By.ID, 'password').send_keys(r['user']['swag_pw'])
        self.driver.find_element(By.ID, 'login-button').click()

    def tearDown(self):
        """Log out"""
        self.driver.find_element(By.CLASS_NAME, 'bm-burger-button').click()
        wait_ = WebDriverWait(self.driver, 10)
        wait_.until(ec.element_to_be_clickable((By.ID, 'logout_sidebar_link')))
        self.driver.find_element(By.ID, 'logout_sidebar_link').click()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_a_shopping(self):
        """check the menu"""
        self.driver.find_element(By.CLASS_NAME, 'bm-burger-button').click()
        wait_ = WebDriverWait(self.driver, 10)
        wait_.until(ec.element_to_be_clickable((By.ID, 'react-burger-cross-btn')))
        time.sleep(1)
        logging.debug('Why still need time before clicking the element after waiting and confirmation?\nLine 52')
        self.driver.find_element(By.ID, 'react-burger-cross-btn').click()

        '''check footer'''
        expected_footer = '© 2024 Sauce Labs. All Rights Reserved. Terms of Service | Privacy Policy'
        actual_footer = self.driver.find_element(By.CLASS_NAME, 'footer_copy').text
        self.assertEqual(expected_footer, actual_footer, 'Not Equal')

        '''check inventories sorter'''
        index = 0
        for i in range(3):
            index = index + 1
            sorter = self.driver.find_element(By.XPATH, "//select[@class='product_sort_container']")
            Select(sorter).select_by_index(index)
        self.driver.find_element(By.CLASS_NAME, 'inventory_item_img').click()
        self.driver.find_element(By.ID, 'back-to-products').click()

        '''choose product(s)'''
        add_to_cart_bt = self.driver.find_elements(By.CLASS_NAME, "btn_inventory")
        for bt in add_to_cart_bt[:2]:
            bt.click()

        '''open cart'''
        cart_link = self.driver.find_elements(By.CLASS_NAME, "shopping_cart_link")
        for bt in cart_link:
            bt.click()
        self.driver.find_element(By.ID, 'checkout').click()

        '''filling address'''
        self.driver.find_element(By.ID, 'first-name').send_keys(r['user']['first_name'])
        self.driver.find_element(By.ID, 'last-name').send_keys(r['user']['last_name'])
        self.driver.find_element(By.ID, 'postal-code').send_keys(r['user']['zip_code'])
        self.driver.find_element(By.ID, 'continue').click()

        '''payment confirmation'''
        self.driver.find_element(By.CLASS_NAME, 'cart_list').is_displayed()
        self.driver.find_element(By.CLASS_NAME, 'summary_info').is_displayed()
        self.driver.find_element(By.ID, 'finish').click()

        '''Thank You Page'''
        act_ty = self.driver.find_element(By.CLASS_NAME, 'complete-header').text
        ec_ty = 'Thank you for your order!'
        self.assertEqual(ec_ty, act_ty, 'Not Thank You Message!')
        self.driver.find_element(By.ID, 'back-to-products').click()

    def test_b_blank_filling(self):
        logging.info('Shopping test is succeed')
        self.driver.refresh()
        """check the menu"""
        self.driver.find_element(By.CLASS_NAME, 'bm-burger-button').click()
        wait = WebDriverWait(self.driver, 2)
        cross_btn = wait.until(ec.element_to_be_clickable((By.ID, "react-burger-cross-btn")))
        time.sleep(0.5)
        cross_btn.click()

        '''check footer'''
        expected_footer = '© 2024 Sauce Labs. All Rights Reserved. Terms of Service | Privacy Policy'
        actual_footer = self.driver.find_element(By.CLASS_NAME, 'footer_copy').text
        self.assertEqual(actual_footer, expected_footer, 'Footer is not match')

        '''check inventories sorter'''
        index = 0
        for i in range(3):
            index = index + 1
        sorter = self.driver.find_element(By.XPATH, "//select[@class='product_sort_container']")
        Select(sorter).select_by_index(index)
        self.driver.find_element(By.CLASS_NAME, 'inventory_item_img').click()
        self.driver.find_element(By.ID, 'back-to-products').click()

        '''choose product(s)'''
        add_to_cart_bt = self.driver.find_elements(By.CLASS_NAME, "btn_inventory")
        for bt in add_to_cart_bt[:2]:
            bt.click()

        '''open cart'''
        cart_link = self.driver.find_elements(By.CLASS_NAME, "shopping_cart_link")
        for bt in cart_link:
            bt.click()
        self.driver.find_element(By.ID, 'checkout').click()

        '''empty form'''
        self.driver.find_element(By.ID, 'continue').click()
        error_message = 'Error: First Name is required'
        actual_message = self.driver.find_element(By.XPATH, "//h3[normalize-space()"
                                                            "='Error: First Name is required']")
        assert error_message in actual_message.text
        logging.info('Blank address filling test is succeed')


if __name__ == "__main__":
    unittest.main()
