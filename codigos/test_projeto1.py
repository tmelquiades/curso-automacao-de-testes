## PASSOS ##
# Logar no site com o usuário standard
# Adicionar os 6 produtos no carrinho
# Conferir que no carrinho tem a badge com 6 produtos
# Entrar no carrinho
# Remover um dos produtos do carrinho
# Conferir que no carrinho tem a badge com 5 produtos
# Clicar no botão Checkout
# Preencher os dados solicitados e clicar em Continue
# Clicar no botão Finish
# Conferir a mensagem “Thank you for your order!”

import pytest
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")
    sleep(2)
    yield driver
    driver.quit()

# teste principal "happy path". tem que passar
def test_happy_path(driver):
    
    # logar com o usuário standard
    standard_user = driver.find_element(By.XPATH, '//*[@id="user-name"]')
    standard_user.send_keys("standard_user")

    standard_user_pwd = driver.find_element(By.XPATH, '//*[@id="password"]')
    standard_user_pwd.send_keys("secret_sauce")

    login_button = driver.find_element(By.XPATH, '//*[@id="login-button"]')
    login_button.click()

    sleep(2)

    # adicionar 6 produtos no carrinho
    product_1 = driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-backpack"]')
    product_1.click()

    product_2 = driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]')
    product_2.click()

    product_3 = driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]')
    product_3.click()

    product_4 = driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-fleece-jacket"]')
    product_4.click()

    product_5 = driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-onesie"]')
    product_5.click()

    product_6 = driver.find_element(By.XPATH, '//*[@id="add-to-cart-test.allthethings()-t-shirt-(red)"]')
    product_6.click()

    # conferir que no carrinho tem a badge com 6 produtos
    cart_badge_number = driver.find_element(By.XPATH, '//span[@class="shopping_cart_badge"][contains(text(), "6")]')

    # entrar no carrinho
    cart_badge = driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a')
    cart_badge.click()

    # remover um dos produtos do carrinho
    remove_product = driver.find_element(By.XPATH, '//*[@id="remove-sauce-labs-backpack"]')
    remove_product.click()

    sleep(2)

    # conferir que no carrinho tem a badge com 5 produtos
    cart_badge_number = driver.find_element(By.XPATH, '//span[@class="shopping_cart_badge"][contains(text(), "5")]')

    sleep(2)

    # clicar no botão checkout
    checkout_button = driver.find_element(By.XPATH, '//*[@id="checkout"]')
    checkout_button.click()

    sleep(2)

    # preencher os dados solicitados e clicar em continue
    first_name = driver.find_element(By.XPATH, '//*[@id="first-name"]')
    first_name.send_keys("Thaís")

    last_name = driver.find_element(By.XPATH, '//*[@id="last-name"]')
    last_name.send_keys("Melquíades")

    postal_code = driver.find_element(By.XPATH, '//*[@id="postal-code"]')
    postal_code.send_keys("45678910")

    continue_button = driver.find_element(By.XPATH, '//*[@id="continue"]')
    continue_button.click()

    sleep(2)

    # clicar no botão Finish
    finish_button = driver.find_element(By.XPATH, '//*[@id="finish"]')
    finish_button.click()

    sleep(2)

    # conferir a mensagem “Thank you for your order!”
    message = driver.find_element(By.XPATH, '//*[@id="checkout_complete_container"]/h2').text
    assert "Thank you for your order!" in message

    sleep(2)

# teste do error_user. tem que falhar
def test_error_user(driver):
    error_user = driver.find_element(By.XPATH, '//*[@id="user-name"]')
    error_user.send_keys("error_user")

    error_user_pwd = driver.find_element(By.XPATH, '//*[@id="password"]')
    error_user_pwd.send_keys("secret_sauce")

    login_button = driver.find_element(By.XPATH, '//*[@id="login-button"]')
    login_button.click()

    sleep(2)

    product_1 = driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-backpack"]')
    product_1.click()

    product_2 = driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]')
    product_2.click()

    product_3 = driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]')
    product_3.click()

    cart_badge_number = driver.find_element(By.XPATH, '//span[@class="shopping_cart_badge"][contains(text(), "3")]')
    cart_badge = driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a')
    cart_badge.click()

def test_standard_user_logout(driver):
    standard_user = driver.find_element(By.XPATH, '//*[@id="user-name"]')
    standard_user.send_keys("standard_user")

    standard_user_pwd = driver.find_element(By.XPATH, '//*[@id="password"]')
    standard_user_pwd.send_keys("secret_sauce")

    login_button = driver.find_element(By.XPATH, '//*[@id="login-button"]')
    login_button.click()

    sleep(2)

    filter_sort = driver.find_element(By.XPATH, '//*[@id="header_container"]/div[2]/div/span/select/option[2]')
    filter_sort.click()

    sleep(2)

    product_6 = driver.find_element(By.XPATH, '//*[@id="add-to-cart-test.allthethings()-t-shirt-(red)"]')
    product_6.click()

    cart_badge = driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a')
    cart_badge.click()

    sleep (2)

    return_shopping_button = driver.find_element(By.XPATH, '//*[@id="continue-shopping"]')
    return_shopping_button.click()

    sleep(2)

    top_left_menu = driver.find_element(By.XPATH, '//*[@id="react-burger-menu-btn"]')
    top_left_menu.click()
    logout_button = driver.find_element(By.XPATH, '//*[@id="logout_sidebar_link"]')
    logout_button.click

    sleep(2)