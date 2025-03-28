from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get('https://bonigarcia.dev/selenium-webdriver-java/loading-images.html')

wait = WebDriverWait(driver, 10)
wait.until(lambda driver: len(driver.find_elements(By.CSS_SELECTOR, "img")) == 3)

image_src = driver.find_elements(By.CSS_SELECTOR, "img")[2].get_attribute("src")                        
print(image_src)                            

driver.quit()
