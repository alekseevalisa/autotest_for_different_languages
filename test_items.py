import pytest 
from selenium import webdriver
import time

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

def test_button_add_to_basket_exists(browser):
    browser.get(link)
    time.sleep(30)
    button = browser.find_element_by_css_selector('button[class="btn btn-lg btn-primary btn-add-to-basket"]')
    assert button is not None, "There is no button 'Add to basket' on the page"
