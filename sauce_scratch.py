from configparser import ConfigParser
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

r = ConfigParser()
r.read('config.ini')


def verify_element_login(self) -> classmethod:
    """Verifying any substantial elements exist in login page"""
    WebDriverWait(self.driver, 10).until(ec.title_is("Swag Labs"))
    assert 'Username' in self.driver.find_element(By.ID, 'user-name').get_attribute('placeholder')
    assert 'Password' in self.driver.find_element(By.ID, 'password').get_attribute('placeholder')
    assert 'Login' in self.driver.find_element(By.ID, 'login-button').get_attribute('value')
    self.driver.find_element(By.CLASS_NAME, 'login_credentials').is_displayed()
    self.driver.find_element(By.CLASS_NAME, 'login_password').is_displayed()


def login(self) -> classmethod:
    """input correct username and password"""
    self.driver.find_element(By.ID, 'user-name').send_keys(r['user']['swag_id'])
    self.driver.find_element(By.ID, 'password').send_keys(r['user']["swag_pw"])
    self.driver.find_element(By.ID, 'login-button').click()


def check_footer(self) -> classmethod:
    """check footer"""
    actual_footer = self.driver.find_element(By.CLASS_NAME, 'footer_copy').text
    assert '© 2024 Sauce Labs. All Rights Reserved. Terms of Service | Privacy Policy' in actual_footer


def check_menu(self) -> classmethod:
    """check the menu"""
    self.driver.find_element(By.CLASS_NAME, 'bm-burger-button').click()
    WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable((By.ID, 'react-burger-cross-btn')))
    self.driver.find_element(By.ID, 'react-burger-cross-btn').click()


def check_inventories(self) -> classmethod:
    """check inventories sorter"""
    index = 0
    for i in range(3):
        index = index + 1
        sorter = self.driver.find_element(By.XPATH, "//select[@class='product_sort_container']")
        Select(sorter).select_by_index(index)
    self.driver.find_element(By.CLASS_NAME, 'inventory_item_img').click()
    self.driver.find_element(By.ID, 'back-to-products').click()


def choose_products(self) -> classmethod:
    """choose product(s)"""
    add_to_cart_bt = self.driver.find_elements(By.CLASS_NAME, "btn_inventory")
    for bt in add_to_cart_bt[:2]:
        bt.click()


def open_cart(self) -> classmethod:
    """open cart"""
    cart_link = self.driver.find_elements(By.CLASS_NAME, "shopping_cart_link")
    for bt in cart_link:
        bt.click()
    self.driver.find_element(By.ID, 'checkout').click()


def address_filling(self) -> classmethod:
    """address filling"""
    self.driver.find_element(By.ID, 'first-name').send_keys(r['user']['first_name'])
    self.driver.find_element(By.ID, 'last-name').send_keys(r['user']['last_name'])
    self.driver.find_element(By.ID, 'postal-code').send_keys(r['user']['zip_code'])
    self.driver.find_element(By.ID, 'continue').click()


def payment_confirmation(self) -> classmethod:
    """payment confirmation"""
    self.driver.find_element(By.CLASS_NAME, 'cart_list').is_displayed()
    self.driver.find_element(By.CLASS_NAME, 'summary_info').is_displayed()
    self.driver.find_element(By.ID, 'finish').click()


def thank_you(self) -> classmethod:
    """Thank You Page"""
    self.driver.find_element(By.CLASS_NAME, 'complete-header').is_displayed()
    self.driver.find_element(By.ID, 'back-to-products').click()


def logout(self) -> classmethod:
    """Log out"""
    self.driver.find_element(By.CLASS_NAME, 'bm-burger-button').click()
    WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable((By.ID, 'logout_sidebar_link')))
    self.driver.find_element(By.ID, 'logout_sidebar_link').click()
