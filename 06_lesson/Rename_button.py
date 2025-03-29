from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("http://uitestingplayground.com/textinput")

text_input = driver.find_element(By.CSS_SELECTOR, '#newButtonName')

text_input.send_keys("SkyPro")

button = driver.find_element(By.CSS_SELECTOR, '#updatingButton')
button.click()

output_text = driver.find_element(By.CSS_SELECTOR, '#updatingButton').text

print(output_text)
