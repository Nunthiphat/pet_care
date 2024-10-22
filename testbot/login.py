from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
import time

# Set up Edge options and driver
edge_options = Options()
service = Service(executable_path=r'C:\Users\focus\OneDrive\เดสก์ท็อป\finalST\testbot\msedgedriver.exe')
driver = webdriver.Edge(service=service, options=edge_options)

try:
    driver.get("http://localhost:3000/Login/login.html")
    
    email_field = driver.find_element(By.ID, "email")
    email_field.send_keys("Cateater2333@gmail.com")

    password_field = driver.find_element(By.ID, "password")
    password_field.send_keys("soyjob")

    login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    login_button.click()

    time.sleep(3)

    if "Welcome" in driver.page_source:
        print("Login successful!")
    else:
        print("Login failed.")

finally:
    driver.quit()
