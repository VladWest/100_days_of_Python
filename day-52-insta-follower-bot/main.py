from selenium import webdriver
import os
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

INSTA_EMAIL = os.environ.get("INSTA_EMAIL")
INSTA_USERNAME = os.environ.get("INSTA_USERNAME")
INSTA_PASS = os.environ.get("INSTA_PASS")

NUMBER_OF_SCROLL = 10
SIMIlAR_ACCOUNT = "python.hub"

chrome_driver_path = "chromedriver.exe"


class InstaFollower:
    def __init__(self, driver_path):
        self.driver = webdriver.Chrome(executable_path=driver_path)

    def login(self, inst_email, inst_pass):
        self.driver.get('https://www.instagram.com/accounts/login/')
        time.sleep(3)
        e_mail_input = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')
        e_mail_input.send_keys(inst_email)
        time.sleep(3)
        pass_input = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')
        pass_input.send_keys(inst_pass)
        time.sleep(2)
        pass_input.send_keys(Keys.ENTER)
        time.sleep(3)
        not_now_btn = self.driver.find_element_by_xpath('//button[text()="Not Now"]')
        not_now_btn.click()
        time.sleep(3)
        not_now_btn = self.driver.find_element_by_xpath('//button[text()="Not Now"]')
        not_now_btn.click()

    def find_followers(self, similar_account, number_of_scrolls):
        time.sleep(5)
        searchbar = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//input[@ placeholder=\'Search\']')))
        searchbar.clear()
        searchbar.send_keys(similar_account)
        time.sleep(3)
        account_name = self.driver.find_element(By.XPATH, f"//div[contains(text(), '{similar_account}')]")
        account_name.click()
        time.sleep(5)
        followers_list = self.driver.find_element(By.XPATH, f"//div[contains(text(), ' followers')]")
        followers_list.click()
        time.sleep(3)
        pop_up_window = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH,
                                                                                        "//div[@Class='isgrP']")))
        for _ in range(number_of_scrolls):
            self.driver.execute_script('arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight',
                                       pop_up_window)
            time.sleep(3)

    def follow(self):
        all_buttons = self.driver.find_elements_by_css_selector("li button")
        for button in all_buttons:
            if button.text != "Follow":
                pass
            else:
                button.click()
                time.sleep(2)


bot = InstaFollower(driver_path=chrome_driver_path)
bot.login(inst_email=INSTA_EMAIL, inst_pass=INSTA_PASS)
bot.find_followers(SIMIlAR_ACCOUNT, NUMBER_OF_SCROLL)
bot.follow()
