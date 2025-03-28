from selenium import webdriver

driver = webdriver.Chrome()

driver.get("http://uitestingplaygtound.com/ajax")

blue_button = driver.find_element_by_id("ajaxButton")
blue_button.click()

green_text = driver.find_element_by_id("result").text

print(green_text)
