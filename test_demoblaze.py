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
logging.basicConfig(filename='../AutomationTesting_Learning000/logs/test_demoblaze.log',
                    format='%(asctime)s %(levelname)s: %(message)s', filemode='w',
                    encoding='utf-8-sig', level=logging.INFO, force=True)


class TestDemoblaze(unittest.TestCase):
    driver = webdriver.Firefox()

    @classmethod
    def setUpClass(cls):
        """Open webpage"""
        cls.driver.maximize_window()
        cls.driver.get(r['url']['demoblaze'])

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
        self.driver.find_element(By.ID, "loginusername").send_keys(r['user']['blaze_id'])
        self.driver.find_element(By.ID, "loginpassword").send_keys(r['user']['blaze_pw'])
        self.driver.find_element(By.ID, "logInModal").click()
        """Verify Footer"""
        self.driver.find_element(By.CSS_SELECTOR, '.py-5.bg-inverse').is_displayed()


if __name__ == "__main__":
    unittest.main()
