import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
import time
import logging

logger = logging.getLogger('demoblaze-log.log')
logger.setLevel(logging.INFO)
handlr = logging.StreamHandler()
logger.addHandler(handlr)

class TestSauceDemo(unittest.TestCase):

    driver = webdriver.Firefox()

    @classmethod
    def setUpClass(cls):
        """Open webpage"""
        cls.driver.maximize_window()
        cls.driver.get('https://www.demoblaze.com/')

    def setUp(self):
        """Verifiying Elements on Homepage"""
        pass

    def tearDown(self):
        """Logout"""
        pass

    @classmethod
    def tearDownClass(cls):
        """Close browser"""
        cls.driver.quit()

    def test_login(self):
        """Login"""
        self.driver.find_element(By.XPATH, '//*[@id="login2"]').click()
        self.driver.find_element(By.ID, 'loginusername').send_keys('username')
        self.driver.find_element(By.ID, 'loginpassword').send_keys('password')
        self.driver.find_element(By.XPATH, '//*[@id="logInModal"]/div/div/div[3]/button[2]').click()

if __name__ == "__main__":
    unittest.main()
