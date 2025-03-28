from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

driver.get("http://uitestingplayground.com/textinput")

text_input = driver.find_element_by_id("text")

text_input.send_keys("SkyPro")

button = driver.find_element_by_id("change-text")
button.click()

output_text = driver.find_element_by_id("result").text

print(output_text)
