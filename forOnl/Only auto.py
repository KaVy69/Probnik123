from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time


urls = [
    "https://only.digital",

]


footer_elements = [
    {"selector": "footer", "description": "Футер"},
    {"selector": "div.Footer_grid__lfZ34", "description": "Элемент 1 в футере"},
    {"selector": ".footer-class-name-2", "description": "Элемент 2 в футере"},

]


def check_footer(driver, url):
    driver.get(url)
    time.sleep(2)


    for element in footer_elements:
        try:
            driver.find_element(By.CSS_SELECTOR, element["selector"])
            print(f'Найден: {element["description"]} на странице {url}')
        except NoSuchElementException:
            print(f'Не найден: {element["description"]} на странице {url}')


driver = webdriver.Chrome()

try:
    for url in urls:
        check_footer(driver, url)
finally:
    driver.quit()