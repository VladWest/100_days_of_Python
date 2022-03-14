from selenium import webdriver


chrome_driver_path = "chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.python.org/")
# find element by id
# price = driver.find_element_by_id("price_block_id")
# print(price.text)

# How to find element by clas name
# logo = driver.find_element_by_class_name("python-logo")

# How to find element by name
# search_bar = driver.find_element_by_name("q")
# print(search_bar.get_attribute("placeholder"))

# Below I will describe 2 possible ways how to find element without clear path

# First method will be using css selector
# Looking for link to documents on python.org
# documentation_link = driver.find_element_by_css_selector(".documentation-widget a")
# print(documentation_link.text)

# Also, we can find element without any special data using XPath which is the second way
# to find element XPath we simply need to use Chrome Developer Tool and inspet the element and
# Copy -> Copy XPath
# See example below
# We are going too look for "Inform about Bug" button on Python.org
# using XPath = "//*[@id="site-map"]/div[2]/div/ul/li[3]/a"
bug_link = driver.find_element_by_xpath('//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
print(bug_link.text)

# Command below will close one tab created via code when page will be downloaded
driver.close()
# Method quit() will close all browser(not only one tab)

