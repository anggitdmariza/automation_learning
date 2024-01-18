import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging

logger = logging.getLogger('phiro-log.log')
logger.setLevel(logging.INFO)
handlr = logging.StreamHandler()
logger.addHandler(handlr)


class TestPAsset(unittest.TestCase):
    driver = webdriver.Chrome('C:/chromedriver-win32/chromedriver.exe')

    def setUp(self):
        self.driver.get('http://old-demo.securehr.net/')

    def tearDown(self):
        self.driver.quit()

    def test_b_asset(self):
        """input incorrect username and password"""
        self.driver.find_element(By.NAME, "nip").send_keys('Q03160')
        self.driver.find_element(By.NAME, "password").send_keys('hiR0@2016')
        self.driver.find_element(By.CSS_SELECTOR, "button[type='submit'] strong").click()
        self.driver.get('http://old-demo.securehr.net/')
        """input correct username and password"""
        self.driver.find_element(By.NAME, "nip").send_keys('Q03160')
        self.driver.find_element(By.NAME, "password").send_keys('phiR0@2016')
        self.driver.find_element(By.CSS_SELECTOR, "button[type='submit'] strong").click()
        """Pilih Menu Pengaturan - Resource Management - Resource Item"""
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_all_elements_located((By.ID, "mCSB_1_container")))
        """Masuk ke menu Resource Item"""
        self.driver.find_element(By.XPATH, '//*[@id="side-menu"]/li[3]/a').click()
        self.driver.find_element(By.XPATH, '//*[@id="side-menu"]/li[3]/ul/li/a').click()
        self.driver.find_element(By.XPATH, '//*[@id="side-menu"]/li[3]/ul/li/ul/li[1]/a').click()
        """Tambah"""
        logging.info("property img only has img property no such button property or clickable property")
        """Masuk ke menu Reservasi Resource Untuk Mengkonfirmasi Resource Item"""
        self.driver.find_element(By.XPATH, '//*[@id="side-menu"]/li[2]').click()
        self.driver.find_element(By.XPATH, '//*[@id="side-menu"]/li[2]/ul/li/a').click()
        self.driver.find_element(By.XPATH, '//*[@id="side-menu"]/li[2]/ul/li/ul/li/a').click()


if __name__ == "__main__":
    unittest.main()
