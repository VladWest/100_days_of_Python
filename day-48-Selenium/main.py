from selenium import webdriver
from selenium.webdriver.common.by import By


chrome_driver_path = "chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.python.org/")

events_list = {}
i = 1
n = 0
while i <= 5:
    time = driver.find_element_by_xpath(f'//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[{i}]/time')
    name = driver.find_element(by=By.XPATH, value=f'//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[{i}]/a')
    events_list[n] = {"time": time.text, "name": name.text}
    n += 1
    i += 1
print(events_list)

# Angela's solution
# event_times = driver.find_elements_by_css_selector(".event-widget time")
# event_names = driver.find_elements_by_css_selector(".event-widget li a")
# events = {}
#
# for n in range(len(event_times)):
#     events[n] = {
#         "time": event_times[n].text,
#         "name": event_names[n].text,
#     }
# print(events)

# Command below will close one tab created via code when page will be downloaded
driver.close()
# Method quit() will close all browser(not only one tab)

