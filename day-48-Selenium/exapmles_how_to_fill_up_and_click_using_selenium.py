from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


chrome_driver_path = "chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://en.wikipedia.org/wiki/Main_Page")

number_of_articles = driver.find_element(by=By.CSS_SELECTOR, value='#articlecount a')
print(number_of_articles.text)
# For clicking on link we can easily use .click() method
# number_of_articles.click()

all_portals = driver.find_element(by=By.LINK_TEXT, value="All portals")
all_portals.click()

# Looking for search bar and typing Python and press Enter
search = driver.find_element(by=By.NAME, value="search")
search.send_keys("Python")
# search.send_keys(Keys.ENTER)

# Command below will close one tab created via code when page will be downloaded
driver.close()
# Method quit() will close all browser(not only one tab)
