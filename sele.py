from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Chrome()
driver.get("file:///D:/OneDrive%20-%20pdpu.ac.in/Desktop/lab/login.html")

driver.find_element(By.ID, "username").send_keys("admin")
driver.find_element(By.ID, "password").send_keys(12346)
driver.find_element(By.ID, "login").click()


h3=driver.find_element(By.ID, "messgae").text
if h3=="Login Success":
    print("Login successful")
else:
    print("login failed")
    