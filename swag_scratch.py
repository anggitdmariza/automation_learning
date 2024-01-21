import time  # to see the response only
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select


class User:
    def __init__(self, driver):
        self.driver = driver

    def wait_for_element(self, by, value, timeout=10):
        return WebDriverWait(self.driver, timeout).until(ec.presence_of_element_located((by, value)))

    def wait_for_url_contains(self, substring, timeout=10):
        return WebDriverWait(self.driver, timeout).until(ec.url_contains(substring))

    def check_loginpage_elements(self):
        # Verifying every element aspect on the login page
        WebDriverWait(self.driver, 10).until(ec.title_is("Swag Labs"))
        self.driver.find_element(By.ID, 'user-name')
        self.driver.find_element(By.ID, 'password')
        self.driver.find_element(By.ID, 'login-button')
        self.driver.find_element(By.CLASS_NAME, 'login_credentials').is_displayed()
        self.driver.find_element(By.CLASS_NAME, 'login_password').is_displayed()

    def accepted_login(self, username, password):
        # Login with accepted credentials
        self.driver.find_element(By.ID, 'user-name').send_keys(username)
        self.driver.find_element(By.ID, 'password').send_keys(password)
        self.driver.find_element(By.ID, 'login-button').click()

    def click_burger_menu(self):
        self.driver.find_element(By.CLASS_NAME, 'bm-burger-button').click()

    def check_inventory_page_elements(self):
        # Verify elements on the inventory page
        WebDriverWait(self.driver, 10).until(ec.title_is("Swag Labs"))
        self.driver.find_element(By.CLASS_NAME, 'product_sort_container')
        self.driver.find_element(By.CLASS_NAME, 'inventory_item')
        self.driver.find_element(By.CLASS_NAME, 'inventory_item_img')
        self.driver.find_element(By.CLASS_NAME, 'inventory_item_desc')
        self.driver.find_element(By.CLASS_NAME, 'pricebar').is_displayed()
        self.driver.find_element(By.CLASS_NAME, 'btn_inventory').is_displayed()

    def check_menu_elements(self):
        self.click_burger_menu()
        self.wait_for_element(By.ID, 'inventory_sidebar_link').click()
        self.wait_for_element(By.ID, 'reset_sidebar_link').click()
        self.wait_for_element(By.ID, 'about_sidebar_link').click()
        self.wait_for_url_contains('saucelabs.com')
        self.driver.back()
        self.wait_for_element(By.CLASS_NAME, 'bm-burger-button').click()
        self.wait_for_element(By.ID, 'react-burger-cross-btn').click()

    def logout(self):
        try:
            self.wait_for_element(By.CLASS_NAME, 'bm-burger-button').click()
            self.wait_for_element(By.ID, 'logout_sidebar_link').click()
        except Exception as e:
            print(f"Logout failed: {e}")
