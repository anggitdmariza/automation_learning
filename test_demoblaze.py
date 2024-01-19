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
    driver = webdriver.Firefox()

    @classmethod
    def setUpClass(cls):
        """Open webpage"""
        cls.driver.maximize_window()
        cls.driver.get('')

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
        self.driver.find_element(By.ID, 'loginusername').send_keys(r['user']['blaze_id'])
        self.driver.find_element(By.ID, 'loginpassword').send_keys(r['user']['blaze_pw'])
        self.driver.find_element(By.XPATH, '//*[@id="logInModal"]/div/div/div[3]/button[2]').click()
        """Verify Footer"""
        try:
            copyright_footer = self.driver.find_element(By.CSS_SELECTOR, '.py-5.bg-inverse').text
            assert 'Copyright © Product Store 2017' in copyright_footer
            logging.info('The Copyright © Product Store 2017\n')
            logging.warning("It's almost seven years! \n")
            logging.error("Why not updating?\n")
            logging.critical("Does it have expiration?\n")
        except AssertionError:
            logging.warning("\nCopyright Not Found\n")


if __name__ == "__main__":
    unittest.main()
