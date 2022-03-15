from selenium import webdriver
from selenium.webdriver.common.by import By


chrome_driver_path = "chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://en.wikipedia.org/wiki/Main_Page")

number_of_articles = driver.find_element(by=By.CSS_SELECTOR, value='#articlecount a')
print(number_of_articles.text)

# Command below will close one tab created via code when page will be downloaded
driver.close()
# Method quit() will close all browser(not only one tab)

