from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()

driver.get("https://paulocoliveira.github.io/mypages/jobapplication.html")

driver.maximize_window()

sleep(2)

full_name = driver.find_element(By.NAME, "fullName")
full_name.send_keys("Thaís Melquíades")

email = driver.find_element(By.NAME, "email")
email.send_keys("thais@gmail.com")

phone_number = driver.find_element(By.NAME, "phoneNumber")
phone_number.send_keys("8398988989")

Select(driver.find_element(By.ID, "desiredPosition")).select_by_visible_text("Designer")

remote = driver.find_element(By.ID, "location2")
remote.click()

years = driver.find_element(By.ID, "experienceYears")
years.send_keys("5")

html = driver.find_element(By.ID, "skill1")
html.click()

js = driver.find_element(By.ID, "skill3")
js.click()

button = driver.find_element(By.CSS_SELECTOR, "button")
button.click()

message = driver.find_element(By.ID, "successMessage").text

sleep(2)

assert "Submission successful!" in message

print(message)

sleep(3)

driver.quit