from selenium import webdriver
import os
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

PROMISED_DOWN = 150
PROMISED_UP = 10
TWITTER_E_MAIL = os.environ.get("TWITTER_S_E-MAIL")
TWITTER_PASS = os.environ.get("TWITTER_S_PASS")
USER_NAME = "@StepanKotNan"

chrome_driver_path = "chromedriver.exe"
# driver = webdriver.Chrome(executable_path=chrome_driver_path)


class InternetSpeedTwitterBot:

    def __init__(self, driver_path):
        self.driver = webdriver.Chrome(executable_path=driver_path)
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        go_button = self.driver.find_element(by=By.XPATH,
                                             value='//*[@id="container"]/div/div[3]/div/div/div'
                                                   '/div[2]/div[3]/div[1]/a/span[4]')
        go_button.click()
        time.sleep(45)
        down_speed = self.driver.find_element(by=By.XPATH,
                                              value='//*[@id="container"]/div/div[3]/div/div/'
                                                    'div/div[2]/div[3]/div[3]/div/div[3]/div/div/'
                                                    'div[2]/div[1]/div[2]/div/div[2]/span')

        up_speed = self.driver.find_element(by=By.XPATH,
                                            value='//*[@id="container"]/div/div[3]/div/div/'
                                                  'div/div[2]/div[3]/div[3]/div/div[3]/div/'
                                                  'div/div[2]/div[1]/div[3]/div/div[2]/span')

        self.up = float(up_speed.text)
        self.down = float(down_speed.text)
        print(f"Download speed: {self.down}")
        print(f"Upload speed: {self.up}")

    def tweet_at_provider(self, twitter_email, username, password):
        self.driver.get("https://twitter.com/")
        message = f"Robotic notification. Looks my Internet isn't so well again. Download: {self.down}, upload: {self.up}"
        time.sleep(5)
        sign_in = self.driver.find_element(by=By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/'
                                                              'main/div/div/div[1]/div[1]/'
                                                              'div/div[3]/div[5]/a/div')
        sign_in.click()
        time.sleep(5)
        e_mail_input = self.driver.find_element(by=By.XPATH, value='//*[@id="layers"]/div/div/div/'
                                                                   'div/div/div/div[2]/div[2]/div/'
                                                                   'div/div[2]/div[2]/div[1]/div/div/'
                                                                   'div[5]/label/div/div[2]/div/input')
        e_mail_input.send_keys(twitter_email)
        e_mail_input.send_keys(Keys.ENTER)
        time.sleep(5)
        phone_username_input = self.driver.find_element(by=By.XPATH, value='//*[@id="layers"]/div/div/div/'
                                                                           'div/div/div/div[2]/div[2]/div/'
                                                                           'div/div[2]/div[2]/div[1]/div/'
                                                                           'div[2]/label/div/div[2]/div/input')
        phone_username_input.send_keys(username)
        phone_username_input.send_keys(Keys.ENTER)
        time.sleep(5)

        pass_input = self.driver.find_element(by=By.XPATH, value='//*[@id="layers"]/div/div/div/'
                                                                 'div/div/div/div[2]/div[2]/div/div/div[2]/'
                                                                 'div[2]/div[1]/div/div/div[3]/div/label/div/'
                                                                 'div[2]/div[1]/input')
        pass_input.send_keys(password)
        time.sleep(3)
        login_btn = self.driver.find_element(by=By.XPATH, value='//*[@id="layers"]/div/div/div/div/div/div/'
                                                                'div[2]/div[2]/div/div/div[2]/div[2]/div[2]/'
                                                                'div/div[1]/div/div/div')
        login_btn.click()
        # End of login part
        # Copied code for tweet
        time.sleep(3)
        editor = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'DraftEditor-root')))
        editor.click()
        tweet_input = WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable((By.CLASS_NAME, 'public-DraftEditorPlaceholder-root')))
        # Tweet text will be set up here
        ActionChains(self.driver).move_to_element(tweet_input).send_keys(message).perform()
        time.sleep(5)
        tweet_btn = self.driver.find_element(by=By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/'
                                                                'div/div/div/div/div[2]/div/div[2]/div[1]/div/div/'
                                                                'div/div[2]/div[3]/div/div/div[2]/div[3]')
        tweet_btn.click()


bot = InternetSpeedTwitterBot(chrome_driver_path)
bot.get_internet_speed()
bot.tweet_at_provider(twitter_email=TWITTER_E_MAIL, username=USER_NAME, password=TWITTER_PASS)

