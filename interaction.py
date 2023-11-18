from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://orteil.dashnet.org/experiments/cookie/")

button = driver.find_element(By.ID, 'cookie')

timeout = time.time() + 5
delay = time.time() + 60 * 5

items = driver.find_elements(By.CSS_SELECTOR, '#store div')
item_id = [i.get_attribute('id') for i in items]
while time.time() < delay:
    money = driver.find_element(By.ID, 'money').text

    button.click()

    if time.time() > timeout:
        all_prices = []
        element_dict = {}
        upgrades = {}
        item = driver.find_elements(By.CSS_SELECTOR, '#store b')
        for i in item:
            g = i.text
            if g != "":
                all_prices.append(int(g.split('-')[1].strip().replace(',', '')))

        for i in range(len(all_prices)):
            element_dict[all_prices[i]] = item_id[i]


        if ',' in money:
            money = int(money.replace(',', ''))
        for price, item_b in element_dict.items():
            if int(money) >= price:
                upgrades[price] = item_b

        if upgrades:
            max_price = max(upgrades)
            id_ = upgrades[max_price]

            if id_:
                driver.find_element(By.ID, f'{id_}').click()

        upgrades = {}

        timeout = time.time() + 5

money = driver.find_element(By.ID, 'money').text
print(f'in 5min you get: {money}')

driver.quit()
