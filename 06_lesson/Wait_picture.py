from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

driver.get('https://bonigarcia.dev/selenium-webdriver-java/loading-images.html')

images = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.TAG_NAME, 'img'))
)

third_image_src = image[2].get_attribute('src')images

print(third_image_src)
