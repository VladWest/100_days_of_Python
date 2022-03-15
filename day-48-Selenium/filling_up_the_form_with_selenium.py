from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys

chrome_driver_path = "chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("http://secure-retreat-92358.herokuapp.com/")

first_name = driver.find_element(by=By.NAME, value="fName")
first_name.send_keys("Vlad")

last_name = driver.find_element(By.NAME, "lName")
last_name.send_keys("Svystun")

email = driver.find_element(By.NAME, "email")
email.send_keys("vladsv001@gmail.com")

submit = driver.find_element(By.XPATH, '/html/body/form/button')
submit.click()

# Command below will close one tab created via code when page will be downloaded
# driver.close()
# Method quit() will close all browser(not only one tab)
