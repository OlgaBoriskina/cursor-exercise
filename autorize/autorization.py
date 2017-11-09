from selenium.webdriver.support import expected_conditions as expected
from selenium.webdriver.common.by import By

import page

home_lacator = "//ul[@id = 'toggleNav']//a[@href='registration.php']"
user_name = "Helga"
password = "Helga"

def autirize (wait):
    page.login(wait).click()
    page.user(wait).send_keys(user_name)
    page.passw(wait).send_keys(password)
    page.submit(wait).click()