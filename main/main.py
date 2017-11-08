from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from submenu import ActionSubmenu

import cookie_autorization
import unittest

base_url = "http://way2automation.com/way2auto_jquery"


class Test (unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome("chromedriver.exe")
        self.driver.get(base_url)
        self.wait = WebDriverWait(self.driver, 10)
        cookie_autorization.autirize(self.driver)
        self.driver.get(base_url + "/menu.php")

    def test_action_submenu(self):
        submenu = ActionSubmenu(self.driver)
        assert(submenu.action_submenu().is_displayed())

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
