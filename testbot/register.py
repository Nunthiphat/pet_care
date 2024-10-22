from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
import time

edge_service = Service(executable_path='C:/Users/focus/OneDrive/เดสก์ท็อป/finalST/testbot/msedgedriver.exe')
edge_options = Options()

driver = webdriver.Edge(service=edge_service, options=edge_options)

driver.get('http://localhost:3000/register')

driver.find_element(By.ID, 'username').send_keys('testuser')
driver.find_element(By.ID, 'email').send_keys('testuser@example.com')
driver.find_element(By.ID, 'password').send_keys('password123')
driver.find_element(By.ID, 'confirmpassword').send_keys('password123')

driver.find_element(By.XPATH, '//button[text()="Register"]').click()

time.sleep(5)

# Optionally, check for a success message or redirection
# success_message = driver.find_element(By.CLASS_NAME, 'success-message').text  # Adjust class name based on your implementation
# print(success_message)

driver.quit()