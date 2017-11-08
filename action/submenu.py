from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as expected
from selenium.webdriver.common.by import By

menu_locator = "id('ui-id-2')"
submenu_locator = "id('ui-id-3')"
frame_locator = "//iframe[@src='menu/defult2.html']"
menu_with_sub_locator = "//a[@href='#example-1-tab-2']"


class ActionSubmenu:
    def __init__(self, driver):
        self._driver = driver
        self._wait = WebDriverWait(self._driver, 10)

    def switch_to_frame(self):
        frame = self._driver.find_element_by_xpath(frame_locator)
        self._driver.switch_to.frame(frame)

    def action_submenu(self):
        self._wait.until(expected.element_to_be_clickable((By.XPATH, menu_with_sub_locator))).click()
        self.switch_to_frame()
        element = self._wait.until(expected.element_to_be_clickable((By.XPATH, menu_locator)))
        actions = ActionChains(self._driver)
        actions.move_to_element(element).perform()
        submenu_element = self._wait.until(expected.element_to_be_clickable((By.XPATH, submenu_locator)))
        return submenu_element