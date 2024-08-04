from selenium import webdriver
from selenium .webdriver.common.by import By
from selenium .webdriver.support.ui import Select
import time


driver=webdriver.Chrome()
driver.get("https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login")
time.sleep(2)
driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div[1]/div[1]/button").click()
time.sleep(2)
Select(driver.find_element(By.NAME,"userSelect")).select_by_visible_text("Harry Potter")
driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/form/button").click()
time.sleep(2)
customer_name= driver .find_element(By.XPATH,"/html/body/div/div/div[2]/div/div[1]/strong/span"). text
assert customer_name == "Harry Potter"
print("correct user login")


driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div[3]/button[2]").click()
time.sleep(2)
driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div[4]/div/form/div/input").send_keys(10000)
time.sleep(2)
driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div[4]/div/form/button").click()
time.sleep(2)

amount_deposit=driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div[4]/div/span").text
assert amount_deposit=="Deposit Successful"
print("deposit Successful")
time.sleep(2)

driver.find_element(By.XPATH, " /html/body/div/div/div[2]/div/div[3]/button[3]  ").click()
time.sleep(2)
driver.find_element(By.XPATH, " /html/body/div/div/div[2]/div/div[4]/div/form/div/input ").send_keys("10000")
time.sleep(2)
driver.find_element(By.XPATH, " /html/body/div/div/div[2]/div/div[4]/div/form/button  ").click()
time.sleep(2)


amount_Withdrwal=driver.find_element(By.XPATH, " /html/body/div/div/div[2]/div/div[4]/div/span ").text
assert amount_Withdrwal=="Transaction successful"
print("transaction Successful")
time.sleep(2) 



driver.quit()