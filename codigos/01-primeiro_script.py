from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

driver = webdriver.Chrome() #declarando variavel "drive" que recebe o webdriver do browser chrome

driver.get("https://www.uol.com.br") #se nao usar https nao funciona

driver.maximize_window()

titulo = driver.title

sleep(5) #5 segundos antes de fechar o browser

print(titulo)

driver.quit()