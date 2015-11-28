from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("https://facebook.com")

email = "email"
password = "pass"
login="loginbutton"
emailelement = driver.find_element_by_name(email)
passwordelement = driver.find_element_by_name(password)
emailelement.send_keys("nilashis@gmail.com")
passwordelement.send_keys("!Mnbvcxz85")

loginelement = driver.find_element_by_id(login)
loginelement.click()


# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# import unittest
#
# # class AirlineSearch(object):
# #
# #     def __init__(self):
# #         self.tangerine = "And now a thousand years between"
# #
# #     def
#
# class LoginTest(unittest.TestCase):
#
#     def setUp(self):
#         self.driver = webdriver.Firefox()
#         self.driver.get("https://www.facebook.com/")
#
#     def test_Login(self):
#         driver = self.driver
#         fbUsername = "nilashis@gmail.com"
#         fbPassword = "!Mnbvcxz85"
#         emailFieldID = ".//*[@id='email']"
#         passFieldID = ".//*[@id='pass']"
#         loginButtonXPath = ".//input[@value='Log In']"
#         flLogoXpath = "(//a[contains(@href, 'logo')])[1]"
#
#
#         emailFieldElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id(emailFieldID))
#         passFieldElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id(passFieldID))
#         loginButtonElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id(loginButtonXPath))
#
#         emailFieldElement.click()
#         emailFieldElement.clear()
#         emailFieldElement.send_keys(fbUsername)
#
#         passFieldElement.click()
#         passFieldElement.clear()
#         passFieldElement.send_keys(fbPassword)
#         loginButtonElement.click()
#         WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id(flLogoXpath))
#
#
#     def tearDown(self):
#         self.driver.quit()
#
#
#
# if __name__ == '__main__':
# #     unittest.main()
#     test = LoginTest()
#     test.setUp()
#     test.test_Login()
#     test.tearDown()






