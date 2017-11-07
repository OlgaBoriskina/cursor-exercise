from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as expected
from selenium.webdriver.common.by import By

menu_locator = "//a[contains(.,'Courses')]"
submenu_locator = "//ul[@class='dropdown-menu']//a[@href='Jmeter Training/Jmeter_training_noida_delhi.html']"

class ActionSubmenu:
    def __init__(self, driver):
        self.__driver = driver
        self.__wait = WebDriverWait(self.__driver, 10)

    def action_submenu(self):
        element = self.__wait.until(expected.element_to_be_clickable((By.XPATH, menu_locator)))
        actions = ActionChains(self.__driver)
        actions.move_to_element(element).perform()
        submenu_element = self.__wait.until(expected.element_to_be_clickable((By.XPATH, submenu_locator)))
        return submenu_element