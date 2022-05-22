import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException

class LoginGoogleFindElementByIDandName():
    def locate_by_xpath_logingoogle(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("https://www.populix.co/login")
        time.sleep(5)
        driver.find_element(By.XPATH, "//body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/button[2]/span[1]").click()
        time.sleep(5)
        driver.find_element(By.XPATH, "//body[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/form[1]/span[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]").send_keys('noermoehammad42@gmail.com')
        time.sleep(5)
        driver.find_element(By.XPATH, "//body[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/button[1]/span[1]").click()
        time.sleep(5)
        driver.find_element(By.XPATH, "//body[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/form[1]/span[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]").send_keys('Satria123')
        time.sleep(5)
        driver.find_element(By.XPATH, "//body[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/button[1]/div[3]").click()
        time.sleep(5)
findbyxpath = LoginGoogleFindElementByIDandName()
findbyxpath.locate_by_xpath_logingoogle()