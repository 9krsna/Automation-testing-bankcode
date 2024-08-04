from selenium import webdriver
import time 
from selenium .webdriver.common.by import By



driver=webdriver.Chrome()
driver.get("https://www.facebook.com/")
time.sleep(5)
print("browers has opend")
email_field=driver.find_element(By.NAME, "")
email_field.send_keys("krishna yadav")
time.sleep(5)
driver.quit()


