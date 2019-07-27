#1 Programm

#from selenium import webdriver

#driver = webdriver.Chrome()

#driver.get("http://google.com")
#assert "Google" in driver.page_source
#driver.quit()

#2 Programm

from selenium import webdriver
import unittest
from selenium.webdriver.common.keys import Keys
import time


class GoogleSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.google.ru")

    def test_01(self):
        driver = self.driver
        input_field = driver.find_element_by_name("q")
        input_field.send_keys("islam")
        input_field.send_keys(Keys.ENTER)

        time.sleep(2)

    def tearDown(self):
        self.driver.quit()

if __name__=="__main__":
    unittest.main()


