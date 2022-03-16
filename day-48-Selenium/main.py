from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Setting up time for how long bot will work in seconds
TIME_IN_SEC_FOR_BOT = 60
# Setting up how often bot will check for possibility to buy most expensive stuff
UPD_TIME = 2
# Path to the Chrome Driver
chrome_driver_path = "chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
# Setting up page for bot
driver.get("http://orteil.dashnet.org/experiments/cookie/")
# Looking for place for clicking
cookie = driver.find_element(by=By.ID, value="cookie")
# Setting up timer with the moment for check
end = time.time() + TIME_IN_SEC_FOR_BOT
check = round(time.time() + UPD_TIME)

while time.time() <= end:
    cookie.click()
    cur_time = round(time.time())
    # Check if we can buy something
    if cur_time == check:
        # Looking for all elements in list
        money = driver.find_element(by=By.CSS_SELECTOR, value="#money").text
        money_int = int(money.replace(",", ""))

        cursor_text = driver.find_element(by=By.CSS_SELECTOR, value="#buyCursor b").text
        cursor_price = int(cursor_text.split("-")[1].replace(",", ""))

        grandma_text = driver.find_element(by=By.CSS_SELECTOR, value="#buyGrandma b").text
        grandma_price = int(grandma_text.split("-")[1].replace(",", ""))

        factory_text = driver.find_element(by=By.CSS_SELECTOR, value="#buyFactory b").text
        factory_price = int(factory_text.split("-")[1].replace(",", ""))

        mine_text = driver.find_element(by=By.CSS_SELECTOR, value="#buyMine b").text
        mine_price = int(mine_text.split("-")[1].replace(",", ""))

        shipment_text = driver.find_element(by=By.CSS_SELECTOR, value="#buyShipment b").text
        shipment_price = int(shipment_text.split("-")[1].replace(",", ""))

        alchemy_text = driver.find_element(by=By.XPATH, value='//*[@id="buyAlchemy lab"]/b').text
        alchemy_price = int(alchemy_text.split("-")[1].replace(",", ""))

        portal_text = driver.find_element(by=By.CSS_SELECTOR, value="#buyPortal b").text
        portal_price = int(portal_text.split("-")[1].replace(",", ""))

        machine_text = driver.find_element(by=By.XPATH, value='//*[@id="buyTime machine"]/b').text
        machine_price = int(machine_text.split("-")[1].replace(",", ""))

        # Checking for the most expensive stuff and auto click to buy it
        if money_int >= machine_price:
            machine = driver.find_element(by=By.XPATH, value='//*[@id="buyTime machine"]')
            machine.click()
        elif money_int >= portal_price:
            portal = driver.find_element(by=By.CSS_SELECTOR, value="#buyPortal")
            portal.click()
        elif money_int >= alchemy_price:
            alchemy = driver.find_element(by=By.XPATH, value='//*[@id="buyTime machine"]')
            alchemy.click()
        elif money_int >= shipment_price:
            shipment = driver.find_element(by=By.CSS_SELECTOR, value="#buyShipment")
            shipment.click()
        elif money_int >= factory_price:
            factory = driver.find_element(by=By.CSS_SELECTOR, value="#buyFactory")
            factory.click()
        elif money_int >= mine_price:
            mine = driver.find_element(by=By.CSS_SELECTOR, value="#buyMine")
            mine.click()
        elif money_int >= grandma_price:
            grandma = driver.find_element(by=By.CSS_SELECTOR, value="#buyGrandma")
            grandma.click()
        elif money_int >= cursor_price:
            cursor = driver.find_element(by=By.CSS_SELECTOR, value="#buyCursor")
            cursor.click()
        # Update "checker" timer
        check = round(time.time() + UPD_TIME)
# Looking for cookies per second number
cps = driver.find_element(by=By.CSS_SELECTOR, value="#cps").text
# Printing out cookies per second number
print(f"You earned {cps} cookies per second")
# Command below will close one tab created via code when page will be downloaded
driver.close()
# Method quit() will close all browser(not only one tab)
