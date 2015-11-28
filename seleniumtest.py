import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import ElementNotVisibleException



def init_driver():
    driver = webdriver.Firefox()
    driver.wait = WebDriverWait(driver, 5)
    return driver


def lookup(driver, query):
    driver.get("http://www.kayak.com")
    try:
        box = driver.wait.until(EC.presence_of_element_located(
            (By.NAME, "c1252960354-location")))
        button = driver.wait.until(EC.element_to_be_clickable(
            (By.NAME, "c1252960354-submit")))
        box.send_keys(query)
        try:
            button.click()
        except ElementNotVisibleException:
            button = driver.wait.until(EC.visibility_of_element_located(
                (By.NAME, "btnG")))
            button.click()
    except TimeoutException:
        print("Box or Button not found in google.com")



if __name__ == "__main__":
    driver = init_driver()
    lookup(driver, "Orlando, FL")
    time.sleep(5)
    driver.quit()

