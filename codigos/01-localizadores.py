from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()

#acessando site 1
browser.get("https://ecommerce-playground.lambdatest.io/index.php?route=account/login")

browser.maximize_window()

sleep(10)

#encontrando elemento por busca por ID
byid = browser.find_element(By.ID, "input-email")
print(byid)

#por name
byname = browser.find_element(By.NAME, "password")
print(byname)

#acessando site 2
browser.get("https://www.lambdatest.com/selenium-playground/ajax-form-submit-demo")

browser.maximize_window()

sleep(10)

#encontrando elemento por busca por classe
byclass = browser.find_element(By.CLASS_NAME, "btn-dark")
print(byclass)

#acessando site 3
browser.get("https://www.lambdatest.com/selenium-playground/")

browser.maximize_window()

sleep(10)

#encontrando elemento por busca por link_text
bylink = browser.find_element(By.LINK_TEXT, "Ajax Form Submit")
print(bylink)

#por partial_link_test
bypartiallink = browser.find_element(By.PARTIAL_LINK_TEXT, "Codes")
print(bypartiallink)

#por tag_name
bytagname = browser.find_elements(By.TAG_NAME, "a")
print(bytagname)

title = browser.title

print(title)

browser.quit()