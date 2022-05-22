import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException

class LoginManualFindElementByIDandName():
    def locate_by_xpath_loginmanual(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("https://www.populix.co/login")
        time.sleep(5)
        driver.find_element(By.XPATH, "//body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/form[1]/div[1]/div[1]/div[1]/input[1]").send_keys('nursaputra1233@yahoo.com')
        time.sleep(5)
        driver.find_element(By.XPATH, "//body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/form[1]/div[1]/div[2]/div[1]/input[1]").send_keys('Satria123')
        time.sleep(5)
        driver.find_element(By.XPATH, "//body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/form[1]/button[1]/span[1]").click()
        time.sleep(5)
findbyxpath = LoginManualFindElementByIDandName()
findbyxpath.locate_by_xpath_loginmanual()