from selenium import webdriver
from configparser import ConfigParser
import unittest
import swag_scratch
import logging

r = ConfigParser()
r.read('config.ini')
logging.basicConfig(filename='../AutomationTesting_Learning000/logs/test_swag_labs.log',
                    format='%(asctime)s %(levelname)s: %(message)s', filemode='w',
                    encoding='utf-8-sig', level=logging.INFO, force=True)


def test_swag_labs():
    # """Get user data"""
    config = ConfigParser()
    config.read('config.ini')
    username = config['user']['swag_id']
    password = config['user']['swag_pw']

    # """Initate User Instance"""
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('https://www.saucedemo.com/')

    # """"Test Cases: """
    user_instance = swag_scratch.User(driver)
    user_instance.check_loginpage_elements()
    logging.info("Proceed to Login Page")
    user_instance.accepted_login(username, password)
    logging.info("Login succeed")
    user_instance.check_inventory_page_elements()
    logging.info("Inventories all checked")
    user_instance.check_menu_elements()
    logging.info("Menus are intractable")
    user_instance.logout()
    logging.info("Logout succeed\nBack to Login Page")

    # """Close Browser"""
    driver.quit()


if __name__ == "__main__":
    unittest.main()
