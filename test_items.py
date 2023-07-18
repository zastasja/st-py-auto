import time
import pytest
from selenium.webdriver.common.by import By

main_url = 'http://selenium1py.pythonanywhere.com/'
all_products = (By.XPATH, '//*[@id="browse"]/li/ul/li[1]/a')
book_item = (By.XPATH, '//img[@alt="Coders at Work"]')
add_to_backet_btn = (By.XPATH, '//*[@id="add_to_basket_form"]/button')

def test_add_product_btn_available_in_french(browser):
    browser.get(main_url)
    browser.find_element(*all_products).click()
    browser.find_element(*book_item).click()
    check = True if browser.find_element(*add_to_backet_btn) else False
    time.sleep(30)
    assert check == True, 'no button add to basket'
